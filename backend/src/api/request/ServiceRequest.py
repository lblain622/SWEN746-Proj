from flask_restful import reqparse

class ServiceParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True, help='Please provide a title for the service')
        self.parser.add_argument('content', type=str, help='Content of the service is optional')
        self.parser.add_argument('price', type=float, required=True, help='Please provide a valid price')
        self.parser.add_argument('user_id', type=int, required=True, help='A valid user_id is required')

    def parse_args(self):
        return self.parser.parse_args()