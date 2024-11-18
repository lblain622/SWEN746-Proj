from flask_restful import Resource
from flask import jsonify
from db.services import ReviewService
from api.request.ReviewRequest import ReviewParser

class ReviewCreate(Resource):
    def __init__(self):
        self.parser = ReviewParser()

    def post(self):
        args = self.parser.parse_args()
        new_review = ReviewService.create_review(args)
        
        return new_review

class ReviewGet(Resource):
    def get(self, service_id):
        return jsonify(ReviewService.get_reviews(service_id))
