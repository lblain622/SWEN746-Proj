import json
import unittest
from tests.test_utils import *

import datetime
from time import gmtime
import pytz 

now = datetime.datetime.now() # Get the current date and time
gmt = pytz.timezone("US/Pacific")
gmt_time = now.astimezone(gmt)
formatted_date = gmt_time.strftime("%a, %d %b %Y %H:%M:%S GMT") # Format the date and time similar to SQL

class TestFilter(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')

    def test_filter(self):
        expected_result = [[
            [
                1,
                "Web Development",
                "Custom web development service",
                "500.00",
                formatted_date,
                1
            ],
            [
                2,
                "Graphic Design",
                "Logo and branding services",
                "300.00",
                formatted_date,
                2
            ],
            [
                3,
                "SEO Optimization",
                "Search engine optimization service",
                "200.00",
                formatted_date,
                3
            ]
        ], 200]

        api_result = get_rest_call(
            self,
            'http://localhost:5000/filter',
            get_header={'Content-Type': 'application/json'}
        )
#        print(api_result)
        self.assertEqual(api_result, expected_result, 'Filter success')

    def test_filter_service(self):
        expected_result = [
            [], 200
        ]
        api_result = get_rest_call(
            self,
            'http://localhost:5000/filter?service=john_doe',
            get_header={'Content-Type':'application/json'}
        )
        self.assertEqual(api_result, expected_result, 'Filter success')

    def test_filter_price(self):
        expected_result = [[],200]
        api_result = get_rest_call(
            self, 'http://localhost:5000/filter?price=50.01',
            get_header={'Content-Type':'application/json'}            
        )
        self.assertEqual(api_result, expected_result, 'Filter success')

    def test_filter_service_and_price(self):
        expected_result= [[], 200]
        api_result = get_rest_call(
            self, 
            'http://localhost:5000/filter?service=john_doe&price=50.01',
            get_header={'Content-Type':'application/json'}
        )
        self.assertEqual(api_result, expected_result, 'Filter service and price.')

    def test_filter_price_range(self):

        expected_result = [[
            [2, 'Graphic Design', 'Logo and branding services', 300.00, formatted_date, 2],
            [3, 'SEO Optimization', 'Search engine optimization service', 200.00, formatted_date, 3]
        ], 200]
        api_result = get_rest_call(
            self, 
            'http://localhost:5000/filter?priceMin=200.0&priceMax=300.0',
            get_header={'Content-Type':'application/json'}
        )
        self.assertEqual(api_result, expected_result, "The price is in the range.")
