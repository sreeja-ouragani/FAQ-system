# 🤖 AI-Powered FAQ System for iPhone 16

A voice-enabled, GPT-powered FAQ system built to handle product-specific queries (e.g., iPhone 16) using natural language.

---

## 🔍 Overview

This smart FAQ assistant allows users to **ask product-related questions via text or voice**, and get **relevant, conversational responses** using the **OpenAI GPT API**.

Specifically designed for product-based customer support (iPhone 16), it combines:

- 🎙️ **Voice input**
- 🤖 **GPT-generated answers**
- 💬 Natural language understanding

---

## 💡 Key Features

- ✅ **Ask product queries** via voice or text
- 🧠 **GPT-4 powered** intelligent responses (context-aware)
- 🎙️ **Speech-to-text integration** for hands-free input
- 📱 Designed for iPhone 16-specific FAQs (e.g., battery, iOS, Face ID)
- 💬 Conversational format (chat-style UI optional)

---

## ⚙️ Tech Stack

- 🐍 Python (Core logic)
- 🌐 Flask (Optional web server)
- 🔊 `speech_recognition` (Voice input using microphone)
- 🎙️ `pyaudio` (Microphone streaming)
- ✨ OpenAI GPT API (`gpt-3.5` or `gpt-4`)
- 🧠 Custom prompt formatting for iPhone-related queries

---

## 🚀 How It Works

1. User speaks or types a query (e.g., "How do I transfer data from my old iPhone?")
2. Speech input is converted to text using `speech_recognition`
3. Query is sent to OpenAI API with a custom prompt
4. Response is generated and displayed or spoken back

---

## 📂 Project Structure

FAQ-system/
├── app.py # Main file to run the assistant
├── voice_input.py # Voice-to-text logic
├── gpt_handler.py # GPT API calls & prompt handling
├── requirements.txt
└── README.md


---

## 🔧 Setup & Usage


git clone https://github.com/sreeja-ouragani/FAQ-system
cd FAQ-system
pip install -r requirements.txt
python app.py

User: (via mic) "Does iPhone 16 support satellite calling?"
GPT: "Yes, the iPhone 16 introduces expanded satellite support for emergency communication in more countries."

📌 Use Cases
📱 Product support for customers (iPhones, gadgets)

🛠️ Voice-first kiosks or retail assistance

🤖 Embeddable chatbot for product landing pages

✍️ Author
Sreeja Ouragani
B.Tech CSE (AI & ML) | AI Project Builder | GPT Enthusiast
📬 LinkedIn

💡 Future Improvements
Text-to-speech (speak back the GPT response)

Multi-product support (AirPods, MacBook, etc.)

Frontend UI using React 


