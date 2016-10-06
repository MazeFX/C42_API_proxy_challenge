# -*- coding: utf-8 -*-

"""
File: test_api_requests.py
Creator: MazeFX
Date: 03-10-2016

Testing for Calendar42 REST API proxy.
(Currently only for the purpose of the challenge)

Provides tests for correctly directing the incoming requests according to proxy design.
"""

from django.core.urlresolvers import resolve
from django.test import TestCase
from unittest.mock import patch, MagicMock

from C42_API_proxy_challenge.api_requests import get_events_with_subscriptions


class C42RequestsTest(TestCase):

	def setUp(self):
        patcher_cache = patch('C42_API_proxy_challenge.api_requests.cache')
        self.mock_cache = patcher_cache.start()
        self.addCleanup(patcher_cache.stop)

    def test_event_with_subscriptions_url_resolves_to_api_proxy(self):
        found = resolve('/C42/events-with-subscriptions/event_id/')
        self.assertEqual(found.func, get_events_with_subscriptions)

    def test_C42_proxy_get_request_returns_json_object(self):
        event_id = 'd6e66cb0ced8e46102bcfd93ceac51b0_14752373875438'
        response = self.client.get('/C42/events-with-subscriptions/{}/'.format(event_id))
        self.assertEqual(response.json()['id'], event_id)

    def test_do_something(self):
        """
        When do_something is called, cache.set is called exactly one
        """
        mymodel = MyModel()
        mymodel.do_something()
        self.assertEqual(self.mock_cache.set.call_count, 1)

    def test_caching_layer(self):
        self.cache.set(key='marco', value='polo')

        with mock.patch.object(SomeClass, 'workhorse_function') as mocked_method:
            sc = SomeClass()
            sc.get_by_username('marco')

            if mocked_method.called:
                self.fail("This was supposed to be a cache hit")
