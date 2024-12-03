from flask_restful import Resource
from flask import jsonify
from db.services import ProfileService
from api.request.ProfileRequest import  ProfileParser
from werkzeug.exceptions import BadRequest

class ProfileController(Resource):
    def __init__(self):
        self.parser = ProfileParser()

    def get(self, id):
        # Fetch the profile using user_id

        profile = ProfileService.get_profile(id)


        if profile:
            return profile, 200
        else:
            return {"message": "Profile not found"}, 404
    def post(self):
        try:
            data = self.parser.parse_args()
            ProfileService.create_profile(data)
            return {"message": "Profile Created"}, 200
        except Exception as e:
            print(f"Error in ProfileController.post: {e}")
            return {"message": "An unexpected error occurred"}, 500

    def put(self, id):
        # Parse request data profile_id
        try:
            parser = ProfileParser()
            data = parser.parse_args()

            # Update the profile using the service
            result = ProfileService.update_profile(id, data)
            if result:
                return {"message": "Profile updated successfully"},200
            else:
                return {"message": "Profile not found"}, 404
        except Exception as e:
            return {"message": "Error updating profile"}, 500




    def delete(self, id):
        # Delete the profile using the service
        try:
            ProfileService.delete_profile(id)

            return {"message": "Profile deleted successfully"},200
        except Exception as e:
            return {"message": "Error deleting profile"}, 500
