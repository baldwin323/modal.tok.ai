import React from 'react';
import { useHistory } from 'react-router-dom';
import { logout } from '../services/auth';

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
    <div>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Logout;