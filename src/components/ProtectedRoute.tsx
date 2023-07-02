import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { useAuth } from '../services/auth';

interface ProtectedRouteProps {
  component: React.FC;
  path: string;
  exact?: boolean;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ component: Component, ...rest }) => {
  const { currentUser } = useAuth();

  return (
    <Route
      {...rest}
      render={props =>
        currentUser ? <Component {...props} /> : <Redirect to="/login" />
      }
    />
  );
};

export default ProtectedRoute;