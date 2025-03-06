import React from "react";
import "../styles/faq.css";

const FAQDisplay = ({ faqs }) => {
  return (
    <div className="faq-display">
      <h3>AI-Generated FAQs</h3>
      <ul>
        {faqs.map((faq, index) => (
          <li key={index}>
            <strong>Q:</strong> {faq.query}
            <br />
            <strong>A:</strong> {faq.answer}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FAQDisplay;
