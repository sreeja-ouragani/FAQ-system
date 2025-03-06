import os
import pandas as pd
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util
import speech_recognition as sr
import google.generativeai as genai  # ✅ Gemini API import
from preprocessing import extract_product_features  # ✅ Import fix

# Load environment variables
load_dotenv()

# Load Gemini API Key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    print("✅ Gemini API Key Loaded Successfully!")
else:
    print("⚠️ Error: GEMINI_API_KEY not found. Check your .env file.")

# Load sentence embedding model for NLP-based answer retrieval
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load FAQs from CSV (Your dataset: iphone_16_faqs.csv)
faq_file = "iphone_16_faqs.csv"

def load_faq_data(faq_file):
    """Loads FAQ dataset from CSV file."""
    try:
        faq_data = pd.read_csv(faq_file)
        faq_data.columns = faq_data.columns.str.lower()  # Normalize column names
        return faq_data
    except Exception as e:
        print(f"⚠️ Error loading FAQ file: {e}")
        return pd.DataFrame(columns=["question", "answer"])  # Return empty DataFrame if error

faq_data = load_faq_data(faq_file)  # Load FAQ data

def generate_faqs_with_answers(product_name, description, num_questions=5):
    """Generates FAQs along with AI-generated answers using Gemini API."""
    prompt = f"Generate {num_questions} frequently asked questions about {product_name}. Features: {description}.\nFor each question, provide a detailed AI-generated answer."

    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # ✅ Use the correct model
        response = model.generate_content(prompt)
        faqs = response.text.strip().split("\n\n")  # Split questions and answers by paragraphs
        return [faqs[i:i+2] for i in range(0, len(faqs), 2)]  # Group questions with answers

    except Exception as e:
        print(f"⚠️ Error generating FAQs with answers: {e}")
        return []

def generate_answer(product_name, question):
    """Generates an AI answer if it's missing from the dataset using Gemini."""
    prompt = f"Answer this question for {product_name}: {question}"

    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # ✅ Use the correct model
        response = model.generate_content(prompt)
        return response.text.strip()  # ✅ Get AI-generated answer

    except Exception as e:
        print(f"⚠️ Error generating AI answer: {e}")
        return "Sorry, I couldn't generate an answer."

def get_answer(user_query, product_name="iPhone 16"):
    """Finds the best answer from dataset, or generates an AI answer if missing."""
    if faq_data.empty:
        print("⚠️ Warning: FAQ dataset is empty.")
        return generate_answer(product_name, user_query)  # Fallback to AI-generated answer

    if "question" not in faq_data.columns or "answer" not in faq_data.columns:
        print("⚠️ Error: FAQ data missing required columns.")
        return generate_answer(product_name, user_query)

    faq_questions = faq_data["question"].tolist()
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(query_embedding, faq_embeddings)[0]
    best_match_idx = scores.argmax().item()
    best_match_question = faq_data.iloc[best_match_idx]["question"]
    best_match_answer = faq_data.iloc[best_match_idx]["answer"]

    if pd.notna(best_match_answer) and best_match_answer.strip():
        return best_match_answer

    return generate_answer(product_name, best_match_question)

def speech_to_text():
    """Converts speech to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError:
        return "Speech recognition service unavailable."

def format_faqs(faqs):
    """Formats FAQs into structured output with clear separation."""
    formatted_output = "\n## Frequently Asked Questions\n"
    formatted_output += "=" * 80 + "\n"

    for question, answer in faqs:
        short_answer = answer.split(".")[0]  # Extract first sentence only
        formatted_output += f"\n**Q: {question}**\n"
        formatted_output += f"A: {short_answer}...\n"
        formatted_output += "-" * 80 + "\n"

    return formatted_output

def generate_faqs_with_formatted_answers(product_name, description, num_questions=5):
    """Generates FAQs, formats them, and returns structured output."""
    faqs = generate_faqs_with_answers(product_name, description, num_questions)
    return format_faqs(faqs)

# Test with a sample question
if __name__ == "__main__":
    if GEMINI_API_KEY:
        print("✅ Gemini API Key Loaded Successfully!")

    product = "iPhone 16"
    description = "Features include wireless charging, AI-enhanced camera, and 30W fast charging."
    
    faqs_with_answers = generate_faqs_with_formatted_answers(product, description)
    if faqs_with_answers:
        print("\nGenerated FAQs with AI Answers:")
        print(faqs_with_answers)

    user_question = "Does the iPhone 16 support wireless charging?"
    answer = get_answer(user_question)
    print(f"\n🔹 Question: {user_question}")
    print(f"✅ AI Answer: {answer}")
