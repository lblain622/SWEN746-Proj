from flask_restful import Resource, request
from flask import jsonify
from db.services import FilterService
from api.request.SearchRequest import SearchParser

# ACCEPTANCE CRITERIA - Filtering services
# The search should return an exact list of candidates matching the user's keywords.
# The search request should be shown in a suggestion tab with an organized and clear UI.

class Filter(Resource): # sorts allgedly 
    # def __init__(self):
    #     self.parser = SearchParser()

    def get(self):
        #args = self.parser.parse_args() # works in ThunderClient, does not work in tests
        price = request.args.get('price', default=None,type=float)
        service = request.args.get('service', default="",type=str)
        priceMin = request.args.get('priceMin', default=None, type=float)
        priceMax = request.args.get('priceMax', default=None, type=float)
        if (priceMin is not None):
            priceMin = round(float(priceMin), 2)
        if (priceMax  is not None):
            priceMax = round(float(priceMin), 2)
        print(priceMin)
        print(priceMax)
        args = {'price':price, 'service':service, 'priceMin':priceMin, 'priceMax':priceMax}
        result = FilterService.all_services(args)
        return jsonify(result)
