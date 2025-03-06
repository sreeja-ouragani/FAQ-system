import React, { useState } from "react";
import "../styles/faq.css";

const FAQInput = ({ onQuerySubmit }) => {
  const [query, setQuery] = useState("");

  const handleInputChange = (e) => setQuery(e.target.value);

  const handleSubmit = () => {
    if (query.trim()) {
      onQuerySubmit(query);
      setQuery("");
    }
  };

  const handleVoiceInput = () => {
    console.log("🎤 Voice input processing... (To be implemented)");
  };

  return (
    <div className="faq-input">
      <input
        type="text"
        placeholder="Type your query..."
        value={query}
        onChange={handleInputChange}
      />
      <button onClick={handleSubmit}>Type</button>
      <button onClick={handleVoiceInput}>Speak 🎤</button>
    </div>
  );
};

export default FAQInput;
