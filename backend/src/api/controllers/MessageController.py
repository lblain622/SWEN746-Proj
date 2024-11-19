from flask_restful import Resource, reqparse
from src.db.services.MessageService import MessageService

class MessageController(Resource):
    def __init__(self):
        self.message_service = MessageService()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('from_id', type=int, required=True, help='Sender ID is required')
        self.parser.add_argument('to_id', type=int, required=True, help='Receiver ID is required')
        self.parser.add_argument('title', type=str, required=True, help='Title is required')
        self.parser.add_argument('content', type=str, required=True, help='Content is required')

    def post(self):
        args = self.parser.parse_args()
        self.message_service.send_message(args['from_id'], args['to_id'], args['title'], args['content'])
        return {'status': 'success'}, 200

    def get(self, user_id):
        messages = self.message_service.get_messages(user_id)
        return {'messages': messages}, 200
