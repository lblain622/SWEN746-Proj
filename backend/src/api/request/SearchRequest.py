from flask_restful import reqparse

class SearchParser():
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('service', type=str, required=False, help='Please enter username')
        self.parser.add_argument('price', type=float, required=False, help='Enter price')
        self.parser.add_argument('priceMin', type=float, required=False, help='Enter price MIN')
        self.parser.add_argument('priceMax', type=float, required=False, help='Enter price MAX')

    def parse_args(self):
        return self.parser.parse_args()

