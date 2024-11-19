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
        
        return jsonify(new_review)

class ReviewGet(Resource):
    def get(self, review_id):
        return jsonify(ReviewService.get_reviews(review_id))

class ReviewUpdate(Resource):
    def __init__(self):
        self.parser = ReviewParser()

    def put(self, review_id):
        args = self.parser.parse_args()
        return jsonify(ReviewService.update_review(review_id, args))
    
class ReviewDelete(Resource):
    def delete(self, review_id):
        return jsonify(ReviewService.delete_review(review_id))
