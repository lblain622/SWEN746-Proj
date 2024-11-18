from flask_restful import Resource
from flask import jsonify
from db.services import UserService
from api.request.UserRequest import UserParser

class UserCreate(Resource):
    def __init__(self):
        self.parser = UserParser()

    def post(self):
        data = self.parser.parse_args()
        user_id = UserService.create_user(data)
        return jsonify({'id': user_id})

class UserUpdate(Resource):
    def __init__(self):
        self.parser = UserParser()

    def put(self, user_id):
        data = self.parser.parse_args()
        UserService.update_user(user_id, data)
        return jsonify({'message': 'User updated successfully'})

class UserGet(Resource):
    def get(self, user_id):
        user = UserService.get_user(user_id)
        return jsonify(user)
        
class UserDelete(Resource):
    def delete(self, user_id):
        UserService.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'})