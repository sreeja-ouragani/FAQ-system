import speech_recognition as sr
from ai_models import get_answer  # Ensure this function is correctly implemented

def recognize_speech():
    """Captures speech input from the microphone and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak your query...")

        recognizer.adjust_for_ambient_noise(source)  # Reduce noise
        audio = recognizer.listen(source)  # Capture audio input

    try:
        user_query = recognizer.recognize_google(audio)  # Convert to text
        print(f"✅ Recognized Text: {user_query}")
        return user_query
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return None
    except sr.RequestError:
        print("❌ Speech recognition service is unavailable.")
        return None

if __name__ == "__main__":
    print("🔹 Speech Processing Test Started...")
    user_query = recognize_speech()

    if user_query:
        ai_answer = get_answer(user_query)  # Get AI-driven answer
        print(f"🤖 AI Answer: {ai_answer}")
    else:
        print("⚠ No valid input detected.")
