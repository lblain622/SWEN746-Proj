from flask import Flask
from flask_restful import Resource, Api
from api.hello_world import Users
from api.management import *

from api.controllers.ProfileController import ProfileController

from api.controllers.ReviewController import *

from api.controllers.UserController import *
from api.controllers.FilterController import *

app = Flask(__name__)
api = Api(app)

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


if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True)