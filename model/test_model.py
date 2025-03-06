import os
import pandas as pd
from ai_models import get_answer  # Ensure get_answer function is correctly imported
from preprocessing import load_dataset
from speech_processing import recognize_speech  # ✅ Import speech-to-text function

FAQ_FILE = "iphone_16_faqs.csv"
LOG_FILE = "faq_logs.csv"  # File to store user queries and answers

def save_to_csv(query, answer, file_path=LOG_FILE):
    """Saves user queries and answers to a CSV file."""
    try:
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["query", "answer"])
            df.to_csv(file_path, index=False)

        df = pd.read_csv(file_path)
        new_entry = pd.DataFrame([{"query": query, "answer": answer}])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"⚠️ Error saving to log file: {e}")

if __name__ == "__main__":
    print("🔹 AI-Powered FAQ System")
    print("Choose input method:")
    print("1️⃣ Type your query ('type')")
    print("2️⃣ Speak your query ('speak')")
    
    choice = input("Enter 'type' or 'speak': ").strip().lower()

    if choice == "type":
        user_query = input("Enter your query: ").strip()
    elif choice == "speak":
        print("🎤 Speak your query...")
        user_query = recognize_speech()  # Capture voice input
    else:
        print("❌ Invalid choice. Please restart and enter 'type' or 'speak'.")
        exit()

    if user_query:
        answer = get_answer(user_query)
        print(f"\n🔹 Question: {user_query}")
        print(f"✅ AI Answer: {answer}")

        save_to_csv(user_query, answer)  # ✅ Save interaction to log
    else:
        print("⚠ No valid input detected.")
