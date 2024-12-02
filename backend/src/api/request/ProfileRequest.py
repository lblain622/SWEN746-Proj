from flask_restful import reqparse
from flask import jsonify

class ProfileParser():
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("user_id", type=int, required=True, help="User ID is required.")
        self.parser.add_argument("first_name", type=str, required=True, help="First Name is required.")
        self.parser.add_argument("last_name", type=str, required=True, help="Last Name is required.")
        self.parser.add_argument("age", type=int, required=True, help="Age must be an integer.")
        self.parser.add_argument("sex", type=str, required=True, help="Sex is required.")
        self.parser.add_argument("student_id", type=str, required=True, help="Student ID is required.")

    def parse_args(self):
        return self.parser.parse_args()