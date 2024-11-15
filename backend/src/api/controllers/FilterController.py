from flask_restful import Resource
from flask import jsonify
from db.services import FilterService
from api.request.SearchRequest import SearchParser

# Scheduling the services AC
# As freelance student should be able to schedule a service to a designated student.
# As a freelance student, I want to show my availability, so my customers can plan accordingly.

class Filter(Resource): # sorts allgedly 
    def __init__(self):
        pass

    def post(self):
        pass

class UserUpdate(Resource):
    def __init__(self):
        pass

    def put(self, user_id):
        pass

class UserGet(Resource):
    def get(self, user_id):
        pass
        
class UserDelete(Resource):
    def put(self, user_id):
        pass