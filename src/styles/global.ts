import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
  }

  button {
    cursor: pointer;
  }

  input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
  }
`;

export default GlobalStyle;