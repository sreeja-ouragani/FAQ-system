import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/landing.css";
import backgroundImage from "../bg.avif";

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div className="landing-container" style={{ backgroundImage: `url(${backgroundImage})` }}>
      <div className="overlay">
        <h1 className="title">NextGen iGuide</h1>
        <p className="tagline">"The only iPhone guide you'll ever need!"</p>
        <button className="get-started-btn" onClick={() => navigate("/home")}>
          Get Started
        </button>
      </div>
    </div>
  );
};

export default LandingPage;
