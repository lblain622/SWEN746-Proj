from flask_restful import Resource
from flask import jsonify
from db.services import UserService
from api.request.UserRequest import UserParser

class UserLogin(Resource):
    def __init__(self):
        self.parser = UserParser()

    def post(self):
        args = self.parser.parse_args()
        user_login = UserService.verify_user(args)

        return user_login

class UserCreate(Resource):
    def __init__(self):
        self.parser = UserParser()

    def post(self):
        args = self.parser.parse_args()
        new_user = UserService.create_user(args)
        
        return new_user

class UserUpdate(Resource):
    def __init__(self):
        self.parser = UserParser()

    def put(self, user_id):
        args = self.parser.parse_args()
        updated_user = UserService.update_user(user_id, args)
        
        return updated_user

class UserGet(Resource):
    def get(self, user_id):
        return jsonify(UserService.get_user(user_id))
        
class UserDelete(Resource):
    def delete(self, user_id):
        deleted_user = UserService.delete_user(user_id)

        return deleted_user
