from flask_restful import Resource  #NOTE: Import from flask_restful, not python

from db.swen610_db_utils import *

from db.example import rebuild_tables

class Init(Resource):
    def post(self):
        try:
            rebuild_tables()  
            message = {'message': 'Tables rebuilt successfully'}
            print(message) 
            return message, 200
        except Exception as e:
            error_message = {'message': f'Error rebuilding tables: {str(e)}'}
            print(error_message)  
            return error_message, 500   

class Version(Resource):
    def get(self):
        try:
            result = exec_get_one('SELECT VERSION()')  
            if result:
                return {'version': result}, 200  
            else:
                return {'message': 'Unable to fetch DB version'}, 404  
        except Exception as e:
            return {'message': f'Error fetching DB version: {str(e)}'}, 500