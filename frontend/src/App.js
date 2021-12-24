import React from "react";
import "./App.css";
import Routes from "./routes/Routes";
import { BrowserRouter as Router } from "react-router-dom";

export const App = () => {
  return (
    <Router>
      <Routes />
    </Router>
  );
};

export default App;
