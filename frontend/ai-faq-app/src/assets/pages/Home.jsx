import React from "react";
import ProductCard from "../components/ProductCard";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const Home = () => {
  return (
    <div>
      <Navbar />
      <main>
        <ProductCard />
      </main>
      <Footer />
    </div>
  );
};

export default Home;
