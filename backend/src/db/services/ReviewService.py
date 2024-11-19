from ..swen610_db_utils import *

def create_review(data):
    query = '''
        INSERT INTO reviews (rating, feedback, user_id, service_id)
        VALUES (%s, %s, %s, %s);
    '''
    exec_commit(query, (data['rating'], data['feedback'], data['user_id'], data['service_id']))
    return {"message": "Review created successfully"}, 200

def get_reviews(review_id):
    query = '''
        SELECT * FROM reviews
        WHERE id = %s;
    '''
    return exec_get_all(query, (review_id,))

def update_review(review_id, data):
    query = '''
        UPDATE reviews
        SET rating = %s, feedback = %s, user_id = %s, service_id = %s
        WHERE id = %s;
    '''

    rows_affected = exec_commit(query, (data['rating'], data['feedback'], data['user_id'], data['service_id'], review_id))

    if rows_affected == 0:
        return {"message": "Review not found"}, 400
    return {"message": "Review updated successfully"}, 200

def delete_review(review_id):
    query = '''
        DELETE 
        FROM reviews
        WHERE id = %s;
    '''

    rows_affected = exec_commit(query, (review_id,))

    if rows_affected == 0:
        return {"message": "Review not found"}, 400
    return {"message": "Review deleted successfully"}, 200


