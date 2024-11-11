from flask_restful import Resource
from flask import jsonify
from db.services import UserService
from api.request.UserRequest import UserParser

class UserCreate(Resource):
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