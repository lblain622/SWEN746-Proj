import os
from ..swen610_db_utils import *

def get_profile(user_id):
    try{
        query = "
        SELECT * FROM profile
        Join users on user.id = profile.user_is
        WHERE user_id = %s
        "
    }
    pass

def create_profile(data):
    pass

def update_profile(profile_id, data):
    pass

def delete_profile(user_id):
    pass
