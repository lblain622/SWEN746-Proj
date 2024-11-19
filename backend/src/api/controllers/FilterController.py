from flask_restful import Resource, request
from flask import jsonify
from db.services import FilterService
from api.request.SearchRequest import SearchParser
from decimal import Decimal 
# ACCEPTANCE CRITERIA - Filtering services
# The search should return an exact list of candidates matching the user's keywords.
# The search request should be shown in a suggestion tab with an organized and clear UI.

class Filter(Resource): # sorts allgedly 
    def get(self):
        #args = self.parser.parse_args() # works in ThunderClient, does not work in tests
        price = request.args.get('price', default=None,type=str)
        service = request.args.get('service', default="",type=str)
        priceMin = request.args.get('priceMin', default=None, type=str)
        priceMax = request.args.get('priceMax', default=None, type=str)
        # Use Decimal for precise handling of decimals
        price_d = Decimal(price) if price else None
        priceMin_d = Decimal(priceMin) if priceMin else None
        priceMax_d = Decimal(priceMax) if priceMax else None
        args = {'price':price_d, 'service':service, 'priceMin':priceMin_d, 'priceMax':priceMax_d}
        result = FilterService.all_services(args)
        return jsonify(result)
