import React, { useState, useEffect } from "react";
import axios from "axios";
import { APiEndPoints } from "../../ApiEndPoints";
import ProductInformation from "../ProductInfo/Information";
import "./Home.css";

const Home = () => {
  const [productInfo, setProductInfo] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const productVariant = await axios(`${APiEndPoints.PRODUCT_VARIANT_URL}`);

      setProductInfo([...productInfo, ...productVariant.data]);
    };

    fetchData();
  }, []);

  console.log("productInfo", productInfo);

  return (
    <div className="main__container">
      {/* <h1>Coding Test - Mediusware Ltd.</h1> */}
      <ProductInformation productInfo={productInfo} />
    </div>
  );
};

export default Home;
