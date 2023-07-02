import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { signUp } from '../services/auth';
import { SignUpForm, SignUpButton, SignUpInput } from '../styles/SignUpStyles';

const SignUp: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleSignUp = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await signUp(email, password);
      history.push('/');
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <SignUpForm onSubmit={handleSignUp}>
      <SignUpInput
        type="email"
        placeholder="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        required
      />
      <SignUpInput
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        required
      />
      <SignUpButton type="submit">Sign Up</SignUpButton>
    </SignUpForm>
  );
};

export default SignUp;