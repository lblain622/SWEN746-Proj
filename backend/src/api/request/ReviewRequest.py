from flask_restful import reqparse

class ReviewParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('rating', type=int, required=True, help='Rating is required (1-5)')
        self.parser.add_argument('feedback', type=str)
        self.parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        self.parser.add_argument('service_id', type=int, required=True, help='Service ID is required')

    def parse_args(self):
        return self.parser.parse_args()
