'use client';
import React, { useState } from 'react';

export default function CreateData() {
  const [name, setName] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('/api/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name }),
    });

    const data = await response.json();
    console.log(data);
  };

  return (
    <div className="form-wrapper">
      <h1>Insert a new name</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">
          <p>Name:</p>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            placeholder="Insert a name"
          />
        </label>
        <button type="submit">Add</button>
      </form>
    </div>
  );
}