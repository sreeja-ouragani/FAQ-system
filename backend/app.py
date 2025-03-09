import os
import sys
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# Get the absolute path of the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ✅ Always use the absolute path for the FAQ file
FAQ_FILE = os.path.join(project_root, "model", "iphone_16_faqs.csv")
LOG_FILE = os.path.join(project_root, "model", "faq_logs.csv")  # ✅ Logs user queries & answers

# ✅ Logs file path check before loading
print(f"📁 Checking FAQ file at: {FAQ_FILE}")
faq_data = None  # Default to None to prevent crashes
if os.path.exists(FAQ_FILE):
    try:
        print(f"📂 Loading FAQ file from: {FAQ_FILE}")
        faq_data = pd.read_csv(FAQ_FILE, encoding='utf-8')  # ✅ Handles special characters
        print("✅ FAQ file loaded successfully!")
    except Exception as e:
        print(f"⚠️ Error loading FAQ file: {e}")
else:
    print(f"❌ Error: FAQ file not found at {FAQ_FILE}")

# Add `model/` folder to Python’s module path
sys.path.append(os.path.join(project_root, "model"))

# Import AI-related functions
from test_model import process_query, process_speech  
from ai_models import get_answer  # ✅ Ensure get_answer is correctly imported
from preprocessing import load_dataset
from speech_processing import recognize_speech  # ✅ Import speech-to-text function

# Initialize Flask app
app = Flask(__name__)

# ✅ Enable CORS for all origins
CORS(app, resources={r"/*": {"origins": "*"}})

def save_to_csv(query, answer, file_path=LOG_FILE):
    """Saves user queries and answers to a CSV file."""
    try:
        if not os.path.exists(file_path):
            pd.DataFrame(columns=["query", "answer"]).to_csv(file_path, index=False)
        
        df = pd.read_csv(file_path)
        new_entry = pd.DataFrame([{"query": query, "answer": answer}])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"⚠️ Error saving to log file: {e}")

@app.route('/generate-faq', methods=['POST'])
def generate_faq():
    """Handles text-based FAQ generation."""
    data = request.get_json()
    user_query = data.get('query', '').strip()

    if not user_query:
        return jsonify({'error': 'No query provided'}), 400

    response = get_answer(user_query)  # ✅ AI-generated answer
    save_to_csv(user_query, response)  # ✅ Log queries
    return jsonify({'faq': {'query': user_query, 'answer': response}})

@app.route('/generate-faq-speech', methods=['POST'])
def generate_faq_speech():
    """Handles speech-based FAQ generation."""
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    user_query = recognize_speech(audio_file)  # ✅ Convert speech to text

    if not user_query:
        return jsonify({'error': 'Speech not recognized'}), 400

    response = get_answer(user_query)  # ✅ AI-generated response
    save_to_csv(user_query, response)  # ✅ Log speech queries
    return jsonify({'faq': {'query': user_query, 'answer': response}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
