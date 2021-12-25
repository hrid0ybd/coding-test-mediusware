import React from "react";

const Information = (props) => {
  return (
    <div>
      <h1>Product</h1>
      {props.productInfo.map((info, index) => {
        console.log("Info", info);
        return (
          <div key={info.id}>
            <h1>{info.id}</h1>
            {info.product_id === 1 ? <h1>HH</h1> : ""}
          </div>
        );
      })}
    </div>
  );
};

export default Information;
