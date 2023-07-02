import firebase from './firebase';

export const signUp = async (email: string, password: string) => {
  try {
    await firebase.auth().createUserWithEmailAndPassword(email, password);
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
};

export const signIn = async (email: string, password: string) => {
  try {
    await firebase.auth().signInWithEmailAndPassword(email, password);
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
};

export const signOut = async () => {
  try {
    await firebase.auth().signOut();
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
};

export const checkAuth = () => {
  return new Promise((resolve) => {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        resolve(true);
      } else {
        resolve(false);
      }
    });
  });
};