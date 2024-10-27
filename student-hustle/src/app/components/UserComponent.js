'use client';

import { useEffect, useState } from "react";
import { getAllUsers } from "@/services/UserService";

export default function UserComponent() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        const fetchUsers = async () => {
            const userData = await getAllUsers();
            setUsers(userData);
        };

        fetchUsers();
    }, []);

    return (
        <div>
            <h1>User List</h1>
            <ul>
                {users.map((user) => (
                    <li key={user.id}>{user.name}</li>
                ))}
            </ul>
        </div>
    );
}