from flask import jsonify
from flask_restful import Resource

from db.services import FilterService
from api.request.SearchRequest import SearchParser

# ACCEPTANCE CRITERIA 
# The availability must exactly match the user's entered timeframed.
# Ensure that services are marked as unavailable once they are booked to avoid confusion to other students.

class Scheduler(Resource): # sorts allgedly 
    def __init__(self):
        pass

    def post(self):
        pass
