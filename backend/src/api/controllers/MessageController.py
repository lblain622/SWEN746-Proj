from flask import request
from flask_restful import Resource
from db.services.MessageService import MessageService
import logging

class MessageController(Resource):
    def __init__(self):
        self.message_service = MessageService()

    def post(self):
        data = request.get_json()
        from_id = data['from_id']
        to_id = data['to_id']
        title = data.get('title', '')
        content = data['content']
        self.message_service.send_message(to_id, from_id, title, content)
        return {'message': 'Message sent successfully'}, 201

    def get(self, user_id=None):
        if user_id:
            logging.info(f"Fetching messages for user_id: {user_id}")
            messages = self.message_service.get_messages(user_id)
            return {'messages': messages}, 200
        else:
            from_id = request.args.get('fromId')
            to_id = request.args.get('toId')
            if from_id and to_id:
                logging.info(f"Fetching conversation between from_id: {from_id} and to_id: {to_id}")
                messages = self.message_service.get_conversation(from_id, to_id)
                return {'messages': messages}, 200
            logging.warning("Invalid request: Missing fromId or toId")
            return {'message': 'Invalid request'}, 400
