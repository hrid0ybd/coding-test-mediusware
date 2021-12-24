import React from "react";
import {
  BrowserRouter as Router,
  Redirect,
  Route,
  Switch,
} from "react-router-dom";

import Home from "../components/Home/Home";
import Navigation from "../components/Navigation/Navigation";

export const Routes = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Redirect to="/home" />
        </Route>
        <Route exact path="/home" component={Home} />
        <Route exact path="/navigation" component={Navigation} />
      </Switch>
    </Router>
  );
};

export default Routes;
