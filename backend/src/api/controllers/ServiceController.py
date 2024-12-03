from flask_restful import Resource
from flask import jsonify
from db.services import ServiceService
from api.request.ServiceRequest import ServiceParser

class ServiceList(Resource):
    def get(self):
        services = ServiceService.list_of_services()
        return jsonify(services)

class ServiceUser(Resource):
    def get(self,user_id):
        services= ServiceService.get_services_user(user_id)
        return jsonify(services)

class ServiceCreate(Resource):
    def __init__(self):
        self.parser = ServiceParser()

    def post(self):
        args = self.parser.parse_args()
        new_service = ServiceService.create_service(args)
        return new_service

class ServiceUpdate(Resource):
    def __init__(self):
        self.parser = ServiceParser()

    def put(self, service_id):
        args = self.parser.parse_args()
        updated_service = ServiceService.update_service(service_id, args)
        return updated_service

class ServiceGet(Resource):
    def get(self, service_id):
        service = ServiceService.get_service(service_id)
        return jsonify(service)

class ServiceDelete(Resource):
    def delete(self, service_id):
        deleted_service = ServiceService.delete_service(service_id)
        return deleted_service
