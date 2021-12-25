import React, { useState, useEffect } from "react";
import axios from "axios";
import { APiEndPoints } from "../../ApiEndPoints";

const Home = () => {
  const [productInfo, setProductInfo] = useState({
    products: [],
    variants: [],
    productVeriants: [],
    productVariantPrices: [],
    productImages: [],
  });

  useEffect(() => {
    const fetchData = async () => {
      const product = await axios(`${APiEndPoints.PRODUCT_URL}`);
      const variant = await axios(`${APiEndPoints.VARIANT_URL}`);
      const productVariant = await axios(`${APiEndPoints.PRODUCT_VARIANT_URL}`);
      const productVariantPrice = await axios(
        `${APiEndPoints.PRODUCT_VARIANT_PRICE_URL}`
      );
      const productImage = await axios(`${APiEndPoints.PRODUCT_IMAGE_URL}`);

      setProductInfo({
        products: [...productInfo.products, ...product.data],
        variants: [...productInfo.variants, ...variant.data],
        productVeriants: [
          ...productInfo.productVeriants,
          ...productVariant.data,
        ],
        productVariantPrices: [
          ...productInfo.productVariantPrices,
          ...productVariantPrice.data,
        ],
        productImages: [
          ...productInfo.productVariantPrices,
          ...productImage.data,
        ],
      });
    };

    fetchData();
  }, []);
  return (
    <div className="main__container">
      <h1>Coding Test - Mediusware Ltd.</h1>
    </div>
  );
};

export default Home;
