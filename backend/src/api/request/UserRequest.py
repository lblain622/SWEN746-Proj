from flask_restful import reqparse

class UserParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Name is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')

    def parse_args(self):
        return self.parser.parse_args()