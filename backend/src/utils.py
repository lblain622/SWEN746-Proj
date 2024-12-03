
from db.swen610_db_utils import exec_get_all

def replace_username_with_id(url):
    import re
    pattern = re.compile(r'/(\w+@\w+\.\w+)/')
    matches = pattern.findall(url)
    
    for username in matches:
        user_id = get_user_id(username)
        if user_id:
            url = url.replace(username, str(user_id))
    return url

def get_user_id(username):
    query = '''
        SELECT id FROM users WHERE email = %s
    '''
    result = exec_get_all(query, (username,))
    return result[0][0] if result else None