'use client';

import { collection, getDocs } from "firebase/firestore";
import { db } from "@/lib/firebaseAdmin";

export async function getAllUsers() {
    const userData = [];

    const query = await getDocs(collection(db, "collection_test"));

    query.forEach((doc) => {
        userData.push({
            id: doc.id,
            ...doc.data()
        });
    });

    return userData;
}