import styled from 'styled-components';

export const SignUpContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f5f5f5;
`;

export const SignUpForm = styled.form`
  display: flex;
  flex-direction: column;
  width: 300px;
  padding: 20px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
`;

export const SignUpInput = styled.input`
  height: 40px;
  margin-bottom: 20px;
  padding: 0 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
`;

export const SignUpButton = styled.button`
  height: 40px;
  border: none;
  border-radius: 5px;
  color: #fff;
  background-color: #007bff;
  cursor: pointer;

  &:hover {
    background-color: #0056b3;
  }
`;

export const SignUpLink = styled.a`
  margin-top: 10px;
  text-decoration: none;
  color: #007bff;

  &:hover {
    text-decoration: underline;
  }
`;