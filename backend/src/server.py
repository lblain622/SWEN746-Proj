from flask import Flask
from flask_restful import  Api
from api.hello_world import Users
from api.management import *
from backend.src.api.controllers.ProfileController import ProfileController
from backend.src.db.example import rebuild_tables
from api.controllers.ProfileController import ProfileController


app = Flask(__name__)
api = Api(app)

api.add_resource(Init, '/manage/init') #Management API for initializing the DB

api.add_resource(Version, '/manage/version') #Management API for checking DB version

api.add_resource(Users, '/') # test to count all users until remove / test...

# APIs ENDPOINTS



#Profile
api.add_resource(ProfileController, '/profiles', '/profile/<int:id>')

if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True)