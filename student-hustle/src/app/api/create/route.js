// api/create/route.js
import { NextResponse } from 'next/server';
import { db } from '@/firebase/firebaseAdmin';

export async function POST(req) {
  try {
    const body = await req.json();
    const data = body;

    const docRef = await db.collection('collection_test').add(data);

    return NextResponse.json({ message: 'Document created successfully!', id: docRef.id }, { status: 201 });
  } catch (error) {
    return NextResponse.json({ error: 'Failed to create document' }, { status: 500 });
  }
}