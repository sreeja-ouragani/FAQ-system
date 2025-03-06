import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./assets/pages/Home";
import FAQPage from "./assets/pages/FAQPage";
import "./assets/styles/global.css";



const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/faq" element={<FAQPage />} />
      </Routes>
    </Router>
  );
};

export default App;
