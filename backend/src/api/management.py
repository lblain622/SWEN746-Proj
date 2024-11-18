from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python


from backend.src.db.swen610_db_utils import exec_get_one


class Init(Resource):
    def post(self):
        rebuild_tables()

class Version(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))