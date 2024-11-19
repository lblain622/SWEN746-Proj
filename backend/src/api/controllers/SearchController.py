from flask_restful import Resource
from flask import jsonify

from db.services import SearchService

from api.request.SearchRequest import SearchParser

# ACCEPTANCE CRITERIA  Searching services
# The search should return an exact list of candidates matching the user's keywords.
# The search request should be shown in a suggestion tab with an organized and clear UI.

class Search(Resource): # what the user types
    def __init__(self):
        pass

    def get(self):
        pass
