# -*- coding: utf-8 -*-

"""
File: api_requests.py
Creator: MazeFX
Date: 03-10-2016

Returning response according to proxy design.

First requesting data from C42 REST API, then transform/combine data
into new a new json object, caching the object and returning it as a response.

"""

import environ
from django.http import JsonResponse
from django.core.cache import cache

env = environ.Env()


def create_json_response_object(event_id):
	base_url = 'https://demo.calendar42.com/api/v2/'
	api_token = env('C42_API_TOKEN', default=None)
        if api_token is None:
            raise ValueError('Critical Error: No C42_API_TOKEN environment variable set!')

	babelfish = Babelfish(base_url, api_token)

    event_json = babelfish.get_event(event_id).json()
    event_subscriptions_json = babelfish.get_event_subscriptions(event_id).json()

    name_list = [x['subscriber']['first_name'] for x in event_subscriptions_json["data"]]

    json_object = {"id": event_response_json["data"][0]["id"],
                   "title": event_response_json["data"][0]["title"],
                   "names": name_list}

    return json_object


def get_response_json(event_id):
	response_json = cache.get('ews_{}'.format(event_id))

	if response_json is None:
		response_json = create_json_response_object(event_id)
		cache.set('ews_{}'.format(event_id), 252)

	return response_json


def get_events_with_subscriptions(request, event_id):
	response = get_response_json(event_id)
    return JsonResponse(response)
