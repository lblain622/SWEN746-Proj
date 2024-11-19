import json
import unittest
from tests.test_utils import *

class TestFilter(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')

    def test_filter(self):
        expected_result = [[
            [
                "Web Development",
                "Custom web development service",
                "500.00"
            ],
            [
                "Graphic Design",
                "Logo and branding services",
                "300.00"
            ],
            [
                "SEO Optimization",
                "Search engine optimization service",
                "200.00"
            ]
        ], 200]

        api_result = get_rest_call(
            self,
            'http://localhost:5000/filter',
            get_header={'Content-Type': 'application/json'}
        )

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

    def test_filter_service_exist(self):
        expected_result = [
            [
                ['Web Development', 'Custom web development service', '500.00']
            ], 200
        ]
        api_result = get_rest_call(
            self,
            'http://localhost:5000/filter?service=Web Development',
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

    def test_filter_price_exists(self):
        expected_result = [[['Graphic Design', 'Logo and branding services', '300.00']], 200]
        api_result = get_rest_call(
            self, 'http://localhost:5000/filter?price=300.00',
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

    def test_filter_service_and_price_exist(self):
        expected_result = [[], 200]
        api_result = get_rest_call(
            self, 
            'http://localhost:5000/filter?service=Graphic Design&price=200.00',
            get_header={'Content-Type':'application/json'}
        )
        self.assertEqual(api_result, expected_result, 'Filter service and price.')

    def test_filter_price_range(self):
        expected_result = [[
            ['Graphic Design', 'Logo and branding services', '300.00'],
            ['SEO Optimization', 'Search engine optimization service', '200.00']
        ], 200]
        api_result = get_rest_call(
            self, 
            'http://localhost:5000/filter?priceMin=200.00&priceMax=300.00',
            get_header={'Content-Type':'application/json'}
        )

        self.assertEqual(api_result, expected_result, "The price is in the range.")
