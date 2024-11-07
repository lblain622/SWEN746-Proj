import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyBTVcSOnp-Cp6emQlRY0l6XZK1VBLXzWnc",
  authDomain: "swen-746.firebaseapp.com",
  projectId: "swen-746",
  storageBucket: "swen-746.appspot.com",
  messagingSenderId: "877097493850",
  appId: "1:877097493850:web:b31b5d38831f9332217f63",
  measurementId: "G-EHNTEY03T6"
};

const app = initializeApp(firebaseConfig);

const db = getFirestore(app);

export { db };