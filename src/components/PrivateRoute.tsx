import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { useAuth } from '../services/auth';

interface PrivateRouteProps {
  component: React.FC;
  path: string;
  exact: boolean;
}

const PrivateRoute: React.FC<PrivateRouteProps> = ({ component: RouteComponent, ...rest }) => {
  const { currentUser } = useAuth();

  return (
    <Route
      {...rest}
      render={routeProps =>
        !!currentUser ? (
          <RouteComponent {...routeProps} />
        ) : (
          <Redirect to={"/login"} />
        )
      }
    />
  );
};

export default PrivateRoute;