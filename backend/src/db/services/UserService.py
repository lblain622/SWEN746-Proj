import os
from ..swen610_db_utils import *

def get_user(user_id):
    sql = "SELECT * FROM users WHERE id = %s"
    return exec_get_one(sql, (user_id,))

def create_user(data):
    sql = "INSERT INTO users (name, password, email) VALUES (%s, %s, %s) RETURNING id"
    return exec_commit(sql, (data['name'], data['password'], data['email']))

def update_user(user_id, data):
    sql = "UPDATE users SET name = %s, password = %s, email = %s WHERE id = %s"
    return exec_commit(sql, (data['name'], data['password'], data['email'], user_id))

def delete_user(user_id):
    sql = "DELETE FROM users WHERE id = %s"
    return exec_commit(sql, (user_id,))
