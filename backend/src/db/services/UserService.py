import os
from ..swen610_db_utils import *

def get_user(user_id):
    query = '''
        SELECT *
        FROM Users
        WHERE id = %s;
    '''

    return exec_get_one(query, (user_id,))

def get_user_by_username(username):
    query = '''
        SELECT *
        FROM Users
        WHERE username = %s;
    '''

    return exec_get_one(query, (username,))

def create_user(data):
    existing_user = get_user_by_username(data['username'])

    if existing_user:
        return {"message": "User already exists!"}, 400

    query = '''
        INSERT INTO Users (username, password, email)
        VALUES (%s, %s, %s);
    '''

    exec_commit(query, (data['username'], data['password'], data['email']))
    return {"message": "User created successfully"}, 200

def update_user(user_id, data):
    query = '''
        UPDATE Users
        SET username = %s, password = %s, email = %s
        WHERE id = %s;
    '''

    rows_affected = exec_commit(query, (data['username'], data['password'], data['email'], user_id))

    if rows_affected == 0:
        return {"message": "User not found"}, 400
    return {"message": "User updated successfully"}, 200

def delete_user(user_id):
    query = '''
        DELETE 
        FROM Users
        WHERE id = %s;
    '''

    rows_affected = exec_commit(query, (user_id,))

    if rows_affected == 0:
        return {"message": "User not found"}, 400
    return {"message": "User deleted successfully"}, 200

def verify_user(data):
    query = '''
        SELECT * FROM Users
        WHERE username = %s AND password = %s;
    '''

    row_found = exec_get_one(query, (data['username'], data['password']))

    if row_found:
        return {"message": "Success"}, 200
    return {"message": "Denied"}, 400
