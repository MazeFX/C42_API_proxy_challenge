# -*- coding: utf-8 -*-

"""
File: test_C42_API_proxy.py
Creator: MazeFX
Date: 07-10-2016

Testing for Calendar42 REST API proxy.
(Currently only for the purpose of the challenge)

Live testing against the C42 REST API to confirm that the requirements
of the challenge have been achieved.

Test can run against a local development server or run against a live server
via the command:

'python manage.py test tests/functional_test --liveserver=mazefx.pythonanywhere.com
"""


import environ
import json
import requests
import sys

from django.contrib.staticfiles.testing import LiveServerTestCase

env = environ.Env()


class FunctionalTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                cls.live_server_url = None
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.live_server_url:
            if cls.server_url == cls.live_server_url:
                super().tearDownClass()

    def setUp(self):
        self.test_event_id = 'd6e66cb0ced8e46102bcfd93ceac51b0_14752373875438'

        api_token = env('C42_API_TOKEN', default=None)
        if api_token is None:
            self.fail('Test failed! No C42_API_TOKEN environment variable set!')

    def tearDown(self):
        pass

    def test_if_api_proxy_returns_the_correct_json_object(self):
        # Testing is done on just 1 event_id.
        response = requests.get('{}/C42/events-with-subscriptions/{}/'.format("http://127.0.0.1:8000",
                                                                          self.test_event_id))

        if response.status_code != 200:
            raise ValueError(
                'Error; Something went wrong while getting a responce from the targeted server. Starting a bloody war.. again')

        test_return_json = {"id": "d6e66cb0ced8e46102bcfd93ceac51b0_14752373875438",
                            "title": "Drink a cup of coffee with C42 Team",
                            "names": ["API",
                                      "Michel",
                                      "Jasper",
                                      "Bob",
                                      "Dennis",
                                      "Edmon",
                                      "Aslesha",
                                      "Lars"]}

        self.assertEqual(test_return_json, response.json())
