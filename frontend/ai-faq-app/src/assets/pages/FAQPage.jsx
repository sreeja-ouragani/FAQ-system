import React, { useState } from "react";
import Navbar from "../components/Navbar";
import FAQInput from "../components/FAQInput";
import FAQDisplay from "../components/FAQDisplay";
import Footer from "../components/Footer";
import AiModelUI from "../components/AiModelUI";

const FAQPage = () => {
  const [faqs, setFaqs] = useState([]);

  const handleQuerySubmit = (query) => {
    const fakeAnswer = "AI-generated answer will be displayed here.";
    setFaqs([...faqs, { query, answer: fakeAnswer }]);
  };

  return (
    <div>
      <Navbar />
      <main>
        <FAQInput onQuerySubmit={handleQuerySubmit} />
        <FAQDisplay faqs={faqs} />
      </main>
      <Footer />
    </div>
  );
};

export default FAQPage;
