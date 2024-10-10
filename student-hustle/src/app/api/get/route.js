// api/get/route.js
import { NextResponse } from 'next/server';
import { db } from '@/firebase/firebaseAdmin';

export async function GET() {
  try {
    const snapshot = await db.collection('collection_test').get();
    const data = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));

    return NextResponse.json(data, { status: 200 });
  } catch (error) {
    return NextResponse.json({ error: 'Failed to fetch data' }, { status: 500 });
  }
}