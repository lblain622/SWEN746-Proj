import os
from .swen610_db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')
    exec_sql_file('src/db/test_data.sql')

def list_users():
    query = '''
        SELECT *
        FROM users
    '''
    return exec_get_all(query)
