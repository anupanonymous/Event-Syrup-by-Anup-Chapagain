import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getDatabase, ref, set, get, update, remove, onValue } from "firebase/database";

// Your Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBYM3qkNI2UzlYmIR4BCiPDu6DnsF5_crk",
  authDomain: "eventsyrupadmin.firebaseapp.com",
  projectId: "eventsyrupadmin",
  storageBucket: "eventsyrupadmin.appspot.com",
  messagingSenderId: "70049127537",
  appId: "1:70049127537:web:9752c83c8c282c9de44fd0",
  measurementId: "G-3QFLHLF74X",
  databaseURL: "https://eventsyrupadmin-default-rtdb.firebaseio.com" // Add the database URL here
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);

export { database, ref, set, get, update, remove, onValue };
