import React, { useState, useEffect } from "react";
import axios from "axios";
import { APiEndPoints } from "../../ApiEndPoints";
import PersonInformation from "../PersonInfo/PersonInformation";

const Home = () => {
  const [personInfo, setPersonInfo] = useState([]);

  useEffect(() => {
    getAllPersonInfo();
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

  return (
    <div className="main__container">
      <h1>Coding Test - Mediusware Ltd.</h1>
      <PersonInformation personInfo={personInfo} />
    </div>
  );
};

export default Home;
