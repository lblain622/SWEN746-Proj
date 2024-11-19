from flask_restful import reqparse
from flask import jsonify

class ProfileParser():
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('first_name', type=str, required=True, help="First name is required.")
        self.parser.add_argument('last_name', type=str, required=True, help="Last name is required.")
        self.parser.add_argument('age', type=int, required=True, help="Age is required and must be an integer.")
        self.parser.add_argument('sex', type=str, required=True, choices=['M', 'F', 'other'], help="Sex is required and must be 'male', 'female', or 'other'.")
        self.parser.add_argument('student_id', type=str, )
        self.parser.add_argument('user_id', type=int, required=True, help="User ID is required and must be an integer.")

    def parse_args(self):
        return self.parser.parse_args()