import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { login } from '../services/auth';
import { LoginStyles } from '../styles/LoginStyles';

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(email, password);
      history.push('/');
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <LoginStyles>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          id="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          id="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
    </LoginStyles>
  );
};

export default Login;