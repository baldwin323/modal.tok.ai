import React from 'react';
import { useHistory } from 'react-router-dom';
import { logout } from '../services/auth';
import { LogoutButton } from '../styles/LogoutStyles';

const Logout: React.FC = () => {
  const history = useHistory();

  const handleLogout = async () => {
    try {
      await logout();
      history.push('/login');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <LogoutButton onClick={handleLogout}>
      Logout
    </LogoutButton>
  );
};

export default Logout;