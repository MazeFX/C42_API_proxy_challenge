# -*- coding: utf-8 -*-

"""
File: test_url_requests.py
Creator: MazeFX
Date: 03-10-2016

Testing for Calendar42 REST API proxy.
(Currently only for the purpose of the challenge)

Provides tests for correctly directing the incoming requests according to proxy design.
"""

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string, get_template
from django.utils.html import escape

from C42_API_proxy_challenge.url_requests import get_events_with_subscriptions


class RequestsTest(TestCase):

    def test_event_with_subscriptions_url_resolves_to_C42_API(self):
        found = resolve('/events-with-subscriptions/')
        self.assertEqual(found.func, get_events_with_subscriptions)

