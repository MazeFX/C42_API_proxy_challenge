# -*- coding: utf-8 -*-

"""
File: urls.py
Creator: MazeFX
Date: 04-10-2016

Url config for the Calendar42 proxy.

Current expected incoming requests:

* 'GET: /events-with-subscriptions/$EVENT_ID/'
    sent to api_request.get_events_with_subscriptions
"""

from django.conf.urls import url

from .api_requests import get_events_with_subscriptions


urlpatterns = [
    # URL pattern for events with subscriptions
    url(r'events-with-subscriptions/(?P<event_id>\w+)/$', get_events_with_subscriptions, name='events-with-subscriptions'),
]
