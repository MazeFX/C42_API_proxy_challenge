# -*- coding: utf-8 -*-

"""
File: test_babelfish.py
Creator: MazeFX
Date: 05-10-2016

Testing for babelfish.

Using mock module for testing without accessing the external api and enabling
offline testing.

Getting the C42_API_KEY from environment for increased security.

"""

import environ
from django.test import TestCase
from unittest.mock import patch, MagicMock

from C42_API_proxy_challenge.babelfish import Babelfish

env = environ.Env()


class BabelfishTest(TestCase):

    def setUp(self):
        self.demo_url = 'https://demo.calendar42.com/api/v2/'
        self.test_event_id = 'd6e66cb0ced8e46102bcfd93ceac51b0_14752373875438'
        
        api_key = env('C42_API_KEY')
        self.babelfish = Babelfish(demo_url, api_key)

    def test_babelfish_exists(self):
        # if the babelfish exists it proves the non-existence of god QED.
        self.assertEqual(self.babelfish.api_url, self.demo_url)

    @patch('C42_API_proxy_challenge.babelfish.request')
    def test_get_event(self, req):
        event_id = MagicMock()
        self.babelfish.get_event(event_id)
        req.assert_called_once_with('GET', event_id)

    def test_get_event_subscriptions(self):
        self.fail('Build a test function')

    def test_build_request_headers(self):
        self.fail('Build a test function')

    def test_build_request_url(self):
        self.fail('Build a test function')

    def test_query_C42_REST_API(self):
        self.fail('Build a test function')