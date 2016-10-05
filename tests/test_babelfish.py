# -*- coding: utf-8 -*-

"""
File: test_babelfish.py
Creator: MazeFX
Date: 05-10-2016

Testing for babelfish.

Using mock module for testing without accessing the external api and enabling
offline testing.

Getting the C42_API_TOKEN from environment for increased security.

"""

import environ
import json
from django.http import JsonResponse
from django.test import TestCase
from unittest.mock import patch, MagicMock

from C42_API_proxy_challenge.babelfish import Babelfish

env = environ.Env()


class BabelfishTest(TestCase):

    def setUp(self):
        self.demo_url = 'https://demo.calendar42.com/api/v2/'
        self.test_event_id = 'DisasterAreaConcert'

        api_token = env('C42_API_TOKEN', default=None)
        if api_token is None:
            self.fail('Test failed! No C42_API_TOKEN environment variable set!')
        self.babelfish = Babelfish(self.demo_url, api_token)

    def test_babelfish_exists(self):
        # if the babelfish exists it proves the non-existence of god QED.
        self.assertEqual(self.babelfish.api_url, self.demo_url)

    def test_get_event(self):
        with patch.object(self.babelfish, 'query_C42_REST_API') as mocked_query:
            mocked_query.return_value = JsonResponse({'id': 'DisasterAreaConcert'})
            response = self.babelfish.get_event(self.test_event_id)
            self.assertEqual(json.loads(response.content.decode('utf-8'))['id'], self.test_event_id)

    def test_get_event_subscriptions(self):
        with patch.object(self.babelfish, 'query_C42_REST_API') as mocked_query:
            mocked_query.return_value = JsonResponse({'event_id': 'DisasterAreaConcert'})
            response = self.babelfish.get_event_subscriptions(self.test_event_id)
            self.assertEqual(json.loads(response.content.decode('utf-8'))['event_id'], self.test_event_id)

    def test_build_request_headers(self):
        header = self.babelfish.build_request_headers()
        self.assertEqual(header['Authorization'], 'Token {}'.format(self.babelfish.api_token))

    def test_build_request_event_url(self):
        url = self.babelfish.build_request_event_url(self.test_event_id)
        self.assertEqual('{}events/{}/'.format(self.demo_url, self.test_event_id), url)

    def test_build_request_event_subscriptions_url(self):
        url = self.babelfish.build_request_event_subscriptions_url(self.test_event_id)
        self.assertEqual('{}event-subscriptions/?event_ids=[{}]'.format(self.demo_url, self.test_event_id), url)

    @patch('C42_API_proxy_challenge.babelfish.requests.get')
    def test_query_C42_REST_API(self, req):
        url = MagicMock()
        headers = MagicMock()
        self.babelfish.query_C42_REST_API(url, headers)
        req.assert_called_once_with(url, headers=headers)
