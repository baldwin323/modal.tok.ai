import firebase from '../utils/firebase';
import { User } from '../types/user';

export const signUp = async (email: string, password: string): Promise<User | null> => {
  try {
    const response = await firebase.auth().createUserWithEmailAndPassword(email, password);
    return {
      uid: response.user?.uid,
      email: response.user?.email,
    };
  } catch (error) {
    console.error(error);
    return null;
  }
};

export const logIn = async (email: string, password: string): Promise<User | null> => {
  try {
    const response = await firebase.auth().signInWithEmailAndPassword(email, password);
    return {
      uid: response.user?.uid,
      email: response.user?.email,
    };
  } catch (error) {
    console.error(error);
    return null;
  }
};

export const logOut = async (): Promise<void> => {
  try {
    await firebase.auth().signOut();
  } catch (error) {
    console.error(error);
  }
};