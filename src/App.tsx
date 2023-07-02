import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import SignUp from './components/SignUp';
import Logout from './components/Logout';
import PrivateRoute from './components/PrivateRoute';
import { GlobalStyle } from './styles/global';

const App: React.FC = () => {
  return (
    <Router>
      <GlobalStyle />
      <Switch>
        <Route exact path="/login" component={Login} />
        <Route exact path="/signup" component={SignUp} />
        <PrivateRoute exact path="/logout" component={Logout} />
      </Switch>
    </Router>
  );
};

export default App;