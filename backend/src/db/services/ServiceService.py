import os
from ..swen610_db_utils import *

def get_service(service_id):
    query = '''
        SELECT *
        FROM services
        WHERE id = %s;
    '''
    return exec_get_one(query, (service_id,))

def get_services_user(user_id)
    query = '''
            SELECT *
            FROM services
            WHERE user_id = %s;
        '''
        return exec_get_one(query, (user_id,))
def list_of_services():
    query = '''
        SELECT *
        FROM services;
    '''
    return exec_get_all(query,)

def create_service(data):
    query = '''
        INSERT INTO services (title, content, price, user_id)
        VALUES (%s, %s, %s, %s);
    '''
    exec_commit(query, (data['title'], data['content'], data['price'], data['user_id']))
    return {"message": "Service created successfully"}, 200

def update_service(service_id, data):
    query = '''
        UPDATE services
        SET title = %s, content = %s, price = %s
        WHERE id = %s;
    '''
    rows_affected = exec_commit(query, (data['title'], data['content'], data['price'], service_id))

    if rows_affected == 0:
        return {"message": "Service not found"}, 400
    return {"message": "Service updated successfully"}, 200

def delete_service(service_id):
    query = '''
        DELETE
        FROM services
        WHERE id = %s;
    '''
    rows_affected = exec_commit(query, (service_id,))

    if rows_affected == 0:
        return {"message": "Service not found"}, 400
    return {"message": "Service deleted successfully"}, 200
