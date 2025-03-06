import React from "react";
import "../styles/product.css";
import iphone16 from "../iPhone16.webp";
import AiModelUI from "./AiModelUI";

const ProductCard = () => {
  return (
    <div className="product-card">
      {/* Left Side: Product Details */}
      <div className="product-left">
        <img src={iphone16} alt="iPhone 16" className="product-image" />
        <div className="product-details">
          <h2>iPhone 16</h2>
          <p>Experience the future with the latest iPhone 16. AI-enhanced performance.</p>
        </div>

        {/* Price and Add to Cart */}
        <div className="product-footer">
          <span className="product-price">₹1,20,000</span>
          <button className="add-to-cart">Add to Cart</button>
        </div>
      </div>

      {/* Right Side: AI FAQ Section */}
      <div className="faq-section">
        <AiModelUI />
      </div>
    </div>
  );
};

export default ProductCard;
