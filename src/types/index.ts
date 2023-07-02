export interface User {
  uid: string;
  email: string;
  displayName: string;
  photoURL: string;
}

export interface AuthError {
  code: string;
  message: string;
}