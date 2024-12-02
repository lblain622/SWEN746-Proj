import os

from ..swen610_db_utils import *

def get_profile(profile_id):
    """
    Fetch the profile of a user based on user_id.
    """
    try:
        query = '''
        SELECT id,first_name,last_name, age, sex, student_id
        FROM profiles
        WHERE user_id = %s;
        '''
        # Execute the query using your database utility

        result = exec_get_one(query, (profile_id,))

        return result
    except Exception as e:
        print(f"Error fetching profile: {e}")
        return None

def create_profile(data):
    """
    Create a new profile.
    Expected `data` structure:
    {
        'first_name': str,
        'last_name': str,
        'age': int,
        'sex': str,
        'student_id': str,
        'user_id': int
    }
    """
    try:
        query = """
        INSERT INTO profiles (first_name, last_name, age, sex, student_id, user_id)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        values = (
            data['first_name'],
            data['last_name'],
            data['age'],
            data['sex'],
            data['student_id'],
            data['user_id'],
        )
        exec_commit(query, values)
    except Exception as e:
        print(f"Error creating profile: {e}")
        raise

def update_profile(profile_id, data):
    """
    Update an existing profile.
    `data` is a dictionary containing the fields to update.
    """
    try:
        fields = ", ".join([f"{key} = %s" for key in data.keys()])
        query = '''
        Update profiles
        SET first_name = %s,
            last_name = %s,
            age = %s,
            sex = %s,
            student_id = %s
        WHERE id = %s;
        '''

        values = (
            data['first_name'],
            data['last_name'],
            data['age'],
            data['sex'],
            data['student_id'],
            profile_id
        )
        exec_commit(query, values)
        return True
    except Exception as e:
        print(f"Error updating profile: {e}")
        return False

def delete_profile(user_id):
    """
    Delete a profile associated with a user_id.
    """
    try:
        query = '''DELETE FROM profiles WHERE user_id = %s;'''
        exec_commit(query, (user_id,))
        return True
    except Exception as e:
        print(f"Error deleting profile: {e}")
        return False
