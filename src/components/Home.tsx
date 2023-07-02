import React from 'react';
import { useHistory } from 'react-router-dom';
import { useAuth } from '../services/auth';
import '../styles/Home.css';

const Home: React.FC = () => {
  const history = useHistory();
  const { currentUser } = useAuth();

  if (!currentUser) {
    history.push('/login');
    return null;
  }

  return (
    <div className="home">
      <h1>Welcome, {currentUser.email}!</h1>
      <p>This is your home page.</p>
    </div>
  );
};

export default Home;