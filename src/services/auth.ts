import firebase from '../utils/firebase';
import { User } from '../types/user';

export const signUp = async (email: string, password: string): Promise<User> => {
  const response = await firebase.auth().createUserWithEmailAndPassword(email, password);
  return {
    uid: response.user?.uid,
    email: response.user?.email,
  };
};

export const signIn = async (email: string, password: string): Promise<User> => {
  const response = await firebase.auth().signInWithEmailAndPassword(email, password);
  return {
    uid: response.user?.uid,
    email: response.user?.email,
  };
};

export const signOut = async (): Promise<void> => {
  await firebase.auth().signOut();
};

export const onAuthStateChanged = (callback: (user: User | null) => void): void => {
  firebase.auth().onAuthStateChanged((user) => {
    if (user) {
      callback({
        uid: user.uid,
        email: user.email,
      });
    } else {
      callback(null);
    }
  });
};