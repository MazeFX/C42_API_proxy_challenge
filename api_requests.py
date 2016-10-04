# -*- coding: utf-8 -*-

"""
File: api_requests.py
Creator: MazeFX
Date: 03-10-2016

Returning response according to proxy design.

First requesting data from C42 REST API, then transform/combine data
into new a new json object and returning it as a response.

"""

from django.http import JsonResponse


def get_events_with_subscriptions(request, event_id):
    return JsonResponse({'id': event_id})
