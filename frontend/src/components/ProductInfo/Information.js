import React from "react";

const Information = (props) => {
  return (
    <div>
      <h1>Check</h1>
      {props.productInfo.map((item, index) => {
        return (
          <div>
            <h1>{item.product_title}</h1>
          </div>
        );
      })}
    </div>
  );
};

export default Information;
