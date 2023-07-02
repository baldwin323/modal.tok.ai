import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import { signOut } from '../services/auth';
import '../styles/logout.css';

const Logout: React.FC = () => {
  const [error, setError] = useState<string | null>(null);
  const history = useHistory();

  useEffect(() => {
    signOut()
      .then(() => {
        history.push('/login');
      })
      .catch((error) => {
        setError(error.message);
      });
  }, [history]);

  return (
    <div className="logout-container">
      {error && <p className="error">{error}</p>}
      <p>Logging out...</p>
    </div>
  );
};

export default Logout;