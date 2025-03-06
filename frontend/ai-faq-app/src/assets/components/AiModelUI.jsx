import React, { useState } from "react";
import { Mic, Send } from "lucide-react";
import "../styles/aimodel.css";


const AiModelUI = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("Ask me anything about this product!");
  const [suggestedQuestions] = useState([
    "Does it support wireless charging?",
    "What are the key features?",
    "Is it compatible with iOS?",
  ]);

  const handleQuerySubmit = () => {
    if (query.trim() === "") return;
    setResponse(`AI Response for: "${query}"`);
    setQuery("");
  };

  return (
    <div className="faq-container">
      <h3 className="faq-title">Looking for specific info?</h3>

      {/* Input Box */}
      <div className="faq-input-box">
        <input
          type="text"
          className="faq-input"
          placeholder="Ask a question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button className="send-button" onClick={handleQuerySubmit}>
          <Send size={20} />
        </button>
        <button className="mic-button">
          <Mic size={20} />
        </button>
      </div>

      {/* AI Response */}
      <p className="faq-response">{response}</p>

      {/* Suggested Questions */}
      <div className="faq-suggestions">
        {suggestedQuestions.map((q, index) => (
          <button
            key={index}
            className="faq-suggestion"
            onClick={() => setResponse(`AI Response for: "${q}"`)}
          >
            {q}
          </button>
        ))}
      </div>
    </div>
  );
};

export default AiModelUI;
