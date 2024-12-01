from flask import Flask
from flask_restful import Resource, Api
from api.hello_world import Users
from api.management import *

from api.controllers.ProfileController import ProfileController

from api.controllers.ReviewController import *

from api.controllers.UserController import *
from api.controllers.FilterController import *
from api.controllers.NotificationController import NotificationController
from api.controllers.MessageController import MessageController
from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room

from db.services.MessageService import MessageService

import logging

app = Flask(__name__)
CORS(app)
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins="*")  # Initialize SocketIO

# Configure logging
logging.basicConfig(level=logging.INFO)

api.add_resource(Init, '/manage/init') #Management API for initializing the DB

api.add_resource(Version, '/manage/version') #Management API for checking DB version

api.add_resource(Users, '/') # test to count all users until remove / test...

# APIs ENDPOINTS
api.add_resource(UserLogin, '/login')
api.add_resource(UserCreate, '/create/user')
api.add_resource(UserUpdate, '/edit/user/<int:user_id>')
api.add_resource(UserGet, '/obtain/user/<int:user_id>')
api.add_resource(UserDelete, '/delete/user/<int:user_id>')

# FILTER
api.add_resource(Filter, '/filter')

#Profile
api.add_resource(ProfileController, '/profile', '/profile/<int:id>')

#API's for reviews 
api.add_resource(ReviewCreate, '/create/review')
api.add_resource(ReviewGet, '/obtain/review/<int:review_id>')
api.add_resource(ReviewUpdate, '/edit/review/<int:review_id>')
api.add_resource(ReviewDelete, '/delete/review/<int:review_id>')

# API's for notifications
api.add_resource(NotificationController, '/notify/<int:user_id>/<string:notification_type>')

# API's for messages
api.add_resource(MessageController, '/messages', '/messages/<int:user_id>', '/messages/conversation')

@socketio.on('send_message')
def handle_send_message(data):
    from_id = data['from_id']
    to_id = data['to_id']
    content = data['content']
    sender_name = data.get('sender_name', 'Unknown')
    message_service = MessageService()
    message_service.send_message(to_id, from_id, sender_name, content)
    print(f"Sending message from {from_id} to {to_id}: {content}")
    emit('received_message', data, room=int(to_id))  # Emit to the receiver
    emit('message_sent', data, room=int(from_id))  # Emit to the receiver
  # Emit to the sender

@socketio.on('join')
def on_join(data):
    user_id = data['user_id']
    join_room(user_id)
    print(f"User {user_id} joined room {user_id}")

if __name__ == '__main__':
    rebuild_tables()

    if os.getenv('CI') is None:  # Check if running in CI environment
        socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
    else:
        app.run(debug=True)
        print("Running in CI, skipping socketio.run()")