import React, { useState, useEffect } from "react";
import axios from "axios";
import { APiEndPoints } from "../../ApiEndPoints";
import PersonInformation from "../PersonInfo/PersonInformation";
import ProductInformation from "../ProductInfo/Information";

const Home = () => {
  const [personInfo, setPersonInfo] = useState([]);
  const [productInfo, setProductInfo] = useState([]);

  useEffect(() => {
    getAllPersonInfo();
    getAllProductInfo();
  }, []);

  const getAllPersonInfo = () => {
    axios
      .get(APiEndPoints.API_URL)
      .then((response) => {
        const allInfo = response.data;
        setPersonInfo(allInfo);
      })
      .catch((error) => console.error(`Error: ${error}`));
  };
  const getAllProductInfo = () => {
    axios
      .get(APiEndPoints.PRODUCT_URL)
      .then((response) => {
        const productInfo = response.data;
        setProductInfo([...productInfo, productInfo]);
      })
      .catch((error) => console.error(`Error: ${error}`));
  };

  return (
    <div className="main__container">
      <h1>Coding Test - Mediusware Ltd.</h1>
      <PersonInformation personInfo={personInfo} />
      <ProductInformation productInfo={productInfo} />
    </div>
  );
};

export default Home;
