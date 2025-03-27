import React, { useState } from "react";
import axios from "axios";
import "../styles/product.css";
import iphone16 from "../../assets/iphone.webp"; 
import { API_BASE_URL } from "../../config";

const ProductCard = () => {
  const [query, setQuery] = useState("");
  const [faqAnswer, setFaqAnswer] = useState("");
  const [showSubmit, setShowSubmit] = useState(false);
  const [listening, setListening] = useState(false);
  const [liveText, setLiveText] = useState(""); // 🔴 Live speech-to-text state

  const handleInputChange = (e) => {
    setQuery(e.target.value);
    setShowSubmit(e.target.value.trim() !== "");
  };

  const formatResponse = (text) => {
    return text
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>") // Bold text
      .replace(/\n/g, "<br />") // Line breaks
      .replace(/•\s/g, "<li>") // Bullet points
      .replace(/<\/li><br \/>/g, "</li>") // Fix bullet spacing
      .replace(/<\/li>/g, "</li><br />"); // Add space between bullet points
  };

  const handleSubmit = async () => {
    if (!query.trim()) return;

    try {
      const response = await axios.post(`${API_BASE_URL}/generate-faq`, { query });
      const formattedAnswer = formatResponse(response.data.faq.answer);
      setFaqAnswer(formattedAnswer);
    } catch (error) {
      console.error("Error generating FAQ:", error);
    }

    setShowSubmit(false);
  };

  // 🔴 **Updated: Live Speech-to-Text Instead of Just "Listening..."**
  const handleVoiceInput = () => {
    setListening(true);
    setLiveText(""); // Reset live text

    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = true; // 🔴 Capture live speech
    recognition.maxAlternatives = 1;

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setQuery(transcript); // Keep the query visible
      setShowSubmit(true);
      setLiveText(transcript); // 🔴 Show live speech text
    };

    recognition.onend = () => {
      setListening(false);
      handleSubmit(); // Auto-submit after finishing
    };

    recognition.onerror = (event) => {
      console.error("Speech Recognition Error:", event.error);
      setListening(false);
    };

    recognition.start();
  };

  return (
    <div className="product-card">
      <div className="product-left">
        <img src={iphone16} alt="iPhone 16" className="product-image" />
        <div className="product-details">
          <h2>iPhone Pro</h2>
          <p>Experience the power of AI with the all-new iPhone Pro. Sleek design, smarter features.</p>
        </div>
        <div className="product-footer">
          <span className="product-price">₹1,20,000</span>
          <button className="add-to-cart">Add to Cart</button>
        </div>
      </div>

      <div className="faq-section">
        <h3>Looking for specific info? Let AI guide you effortlessly!</h3>
        <div className="faq-input">
          <input
            type="text"
            placeholder="Type your query..."
            value={query} // 🔴 Keeps the question visible
            onChange={handleInputChange}
          />
          <button onClick={handleVoiceInput}>Speak 🎤</button>
          {listening && <span className="listening">🎙 {liveText || "Listening..."}</span>}
          {showSubmit && <button onClick={handleSubmit}>Submit</button>}
        </div>

        {faqAnswer && (
          <div className="faq-answer">
            <h4>AI Answer:</h4>
            <div className="ai-answer-container">
              <p dangerouslySetInnerHTML={{ __html: faqAnswer }} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductCard;
