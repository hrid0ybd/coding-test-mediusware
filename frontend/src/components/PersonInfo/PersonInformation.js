import React from "react";

const PersonInformation = (props) => {
  return (
    <div>
      {props.personInfo.map((info, index) => {
        return (
          <div key={info.id}>
            <h1>{info.name}</h1>
          </div>
        );
      })}
    </div>
  );
};

export default PersonInformation;
