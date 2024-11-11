from flask_restful import Resource
from flask import jsonify
from db.example import *

class Users(Resource):
    def get(self):
        return jsonify(list_users())
