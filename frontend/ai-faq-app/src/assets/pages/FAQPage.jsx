import React, { useState } from "react";
import Navbar from "../components/Navbar";
import ProductCard from "../components/ProductCard";
import Footer from "../components/Footer";
import { API_BASE_URL } from "../../config";

const FAQPage = () => {
  const [faqs, setFaqs] = useState([]);

  const handleQuerySubmit = async (query) => {
    try {
      const response = await fetch(`${API_BASE_URL}/generate-faq`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();
      const cleanAnswer = data.faq.answer.replace(/\s+/g, " ").trim(); // Remove unwanted spaces & newlines
      const newFAQ = { query, answer: cleanAnswer };

      setFaqs([...faqs, newFAQ]);
    } catch (error) {
      console.error("Error fetching AI response:", error);
    }
  };

  return (
    <div>
      <Navbar />
      <main>
        <ProductCard onQuerySubmit={handleQuerySubmit} faqs={faqs} />
      </main>
      <Footer />
    </div>
  );
};

export default FAQPage;
