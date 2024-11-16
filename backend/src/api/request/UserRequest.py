from flask_restful import reqparse

class UserParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Please enter username')
        self.parser.add_argument('password', type=str, required=True, help='Password cannot be empty')
        self.parser.add_argument('email', type=str)

    def parse_args(self):
        return self.parser.parse_args()