from flask import Flask
from flask_restful import Resource, Api
from api.hello_world import Users
from flask_cors import CORS
from api.management import *

from api.controllers.ProfileController import ProfileController
from api.controllers.ReviewController import *
from api.controllers.UserController import *
from api.controllers.FilterController import *
from api.controllers.ServiceController import *

app = Flask(__name__)
CORS(app)
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

# APIs Services
# api.add_resource(ServiceList, '/services')
api.add_resource(ServiceCreate, '/services/create')
# api.add_resource(ServiceUpdate, '/services/update/<int:service_id>')
api.add_resource(ServiceGet, '/services/<int:service_id>')
api.add_resource(ServiceDelete, '/services/delete/<int:service_id>')

# APIs Filter
api.add_resource(Filter, '/filter')

# APIs Profile
api.add_resource(ProfileController, '/profile', '/profile/<int:id>')

# APIs Review
api.add_resource(ReviewCreate, '/create/review')
api.add_resource(ReviewGet, '/obtain/review/<int:review_id>')
api.add_resource(ReviewUpdate, '/edit/review/<int:review_id>')
api.add_resource(ReviewDelete, '/delete/review/<int:review_id>')


if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True)