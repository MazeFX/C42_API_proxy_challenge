# -*- coding: utf-8 -*-

"""
File: test_api_requests.py
Creator: MazeFX
Date: 03-10-2016

Testing for Calendar42 REST API proxy.
(Currently only for the purpose of the challenge)

Provides tests for correctly directing the incoming requests according to proxy design.
"""

import json
import os
from django.core.urlresolvers import resolve
from django.test import TestCase
from unittest.mock import patch, MagicMock

from C42_API_proxy_challenge.api_requests import (get_events_with_subscriptions,
    get_response_json, create_json_response_object)


class C42RequestsTest(TestCase):

    def setUp(self):
        patcher_cache = patch('C42_API_proxy_challenge.api_requests.cache')
        self.mock_cache = patcher_cache.start()
        self.addCleanup(patcher_cache.stop)

        patcher_get_response_json = patch('C42_API_proxy_challenge.api_requests.get_response_json')
        self.mock_get_response_json = patcher_get_response_json.start()
        self.addCleanup(patcher_get_response_json.stop)

        patcher_create_json_response_object = patch('C42_API_proxy_challenge.api_requests.create_json_response_object')
        self.mock_create_json_response_object = patcher_create_json_response_object.start()
        self.addCleanup(patcher_create_json_response_object.stop)

        # Load json files with real objects from C42 REST API
        # for testing json mangling
        with open(os.path.join(os.path.dirname(__file__), 'event_object.json')) as json_data:
            data = json.load(json_data)
            print(data)
        self.test_get_event_response = data

        with open(os.path.join(os.path.dirname(__file__), 'event_subscriptions_object.json')) as json_data:
            data = json.load(json_data)
        self.test_event_subscriptions_response = data

        self.test_event_id = 'DisasterAreaConcert'

    def test_event_with_subscriptions_url_resolves_to_api_proxy(self):
        found = resolve('/C42/events-with-subscriptions/event_id/')
        self.assertEqual(found.func, get_events_with_subscriptions)

    def test_C42_proxy_get_request_returns_json_object(self):
        self.mock_get_response_json.return_value = {'event_id': 'DisasterAreaConcert'}
        response = self.client.get('/C42/events-with-subscriptions/{}/'.format(self.test_event_id))
        self.assertEqual(response.json()['event_id'], self.test_event_id)

    def test_get_response_json(self):
        self.mock_cache.get.return_value = None
        self.mock_create_json_response_object.return_value = {'event_id': 'DisasterAreaConcert'}

        response_json = get_response_json(self.test_event_id)
        self.assertEqual(response_json, {'event_id': 'DisasterAreaConcert'})

    def test_if_get_response_json_is_cached(self):
        self.mock_cache.get.return_value = None
        self.mock_create_json_response_object.return_value = {'event_id': 'DisasterAreaConcert'}

        response_json = get_response_json(self.test_event_id)
        self.assertEqual(self.mock_cache.set.call_count, 1)
        self.mock_cache.set.assert_called_once_with('ews_{}'.format(self.test_event_id),
                                                    {'event_id': 'DisasterAreaConcert'}, 252)

    def test_if_get_response_json_gets_returned_from_cache(self):
        self.mock_cache.get.return_value = {'event_id': 'DisasterAreaConcert'}

        response_json = get_response_json(self.test_event_id)
        self.assertEqual(self.mock_cache.set.call_count, 0)

    @patch('C42_API_proxy_challenge.babelfish.Babelfish.get_event_subscriptions')
    @patch('C42_API_proxy_challenge.babelfish.Babelfish.get_event')
    def test_create_json_response_object(self, mock_get_event, mock_get_event_subscriptions):
        # mock the returning objects from babelfish
        mock_get_event.return_value = self.test_get_event_response
        mock_get_event_subscriptions.json.return_value = self.test_event_subscriptions_response

        json_object = create_json_response_object(self.test_event_id)
        self.assertEqual(json_object["id"], "d6e66cb0ced8e46102bcfd93ceac51b0_14752373875438")
        self.assertEqual(json_object["names"], ["API"])

    # def test_caching_layer(self):
    #     self.cache.set(key='marco', value='polo')
    #
    #     with mock.patch.object(SomeClass, 'workhorse_function') as mocked_method:
    #         sc = SomeClass()
    #         sc.get_by_username('marco')
    #
    #         if mocked_method.called:
    #             self.fail("This was supposed to be a cache hit")
