from flask import Flask
from flask_restful import Resource, Api
from api.hello_world import Users
from api.management import *
from api.controllers.UserController import UserCreate, UserDelete, UserGet, UserUpdate
# from api.controllers.UserController import *
from api.controllers.FilterController import * 

app = Flask(__name__)
api = Api(app)

api.add_resource(Init, '/manage/init') #Management API for initializing the DB

api.add_resource(Version, '/manage/version') #Management API for checking DB version

api.add_resource(Users, '/') # test to count all users until remove / test...

# APIs ENDPOINTS

# USER
api.add_resource(UserCreate, '/user/create')
api.add_resource(UserUpdate, '/user/edit/<int:user_id>')
api.add_resource(UserGet, '/users/<int:user_id>')
api.add_resource(UserDelete, '/user/delete/<int:user_id>')

# FILTER
api.add_resource(Filter, '/filter')

if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True)