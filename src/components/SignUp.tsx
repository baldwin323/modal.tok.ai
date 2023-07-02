import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { signUp } from '../services/auth';
import '../styles/SignUp.css';

const SignUp: React.FC = () => {
  const history = useHistory();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSignUp = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await signUp(email, password);
      history.push('/');
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="signup">
      <form onSubmit={handleSignUp}>
        <h1>Sign Up</h1>
        {error && <p>{error}</p>}
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default SignUp;