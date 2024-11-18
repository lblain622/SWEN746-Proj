from ..swen610_db_utils import *

def create_review(data):
    query = '''
        INSERT INTO reviews (rating, feedback, user_id, service_id)
        VALUES (%s, %s, %s, %s);
    '''
    exec_commit(query, (data['rating'], data['feedback'], data['user_id'], data['service_id']))
    return {"message": "Review created successfully"}, 200

def get_reviews(service_id):
    query = '''
        SELECT * FROM reviews
        WHERE service_id = %s;
    '''
    return exec_get_all(query, (service_id,))
