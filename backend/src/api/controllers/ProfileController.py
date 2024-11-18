from flask_restful import Resource
from flask import jsonify
from ..request.ProfileRequest import  ProfileParser
from backend.src.db.services import ProfileService

class ProfileController(Resource):
    def get(self, user_id):
        # Fetch the profile using the service
        profile = ProfileService.get_profile(user_id)
        if profile:
            return jsonify({"profile": profile})
        else:
            return jsonify({"message": "Profile not found"}), 404
    def post(self):
        # Parse request data
        parser = ProfileParser()
        data = parser.parse_args()

        # Create the profile using the service
        profile_id = ProfileService.create_profile(data)
        if profile_id:
            return jsonify({"message": "Profile created successfully", "profile_id": profile_id})
        else:
            return jsonify({"message": "Error creating profile"}), 500
    def put(self, profile_id):
        # Parse request data
        parser = ProfileParser()
        data = parser.parse_args()

        # Update the profile using the service
        success = ProfileService.update_profile(profile_id, data)
        if success:
            return jsonify({"message": "Profile updated successfully"})
        else:
            return jsonify({"message": "Error updating profile"}), 500




    def delete(self, user_id):
        # Delete the profile using the service
        success = ProfileService.delete_profile(user_id)
        if success:
            return jsonify({"message": "Profile deleted successfully"})
        else:
            return jsonify({"message": "Error deleting profile"}), 500
