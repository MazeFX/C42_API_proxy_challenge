# -*- coding: utf-8 -*-

"""
File: babelfish.py
Creator: MazeFX
Date: 04-10-2016

A fish that is so mind-bogglingly useful that it can communicate
with the C42 REST API.

api_key gets passed in to enable future support for different api-keys and
associated system rights. Multiple apps can acces Babelfish with different
profiles and abilities.
"""


import requests


class Babelfish(object):

    def __init__(self, base_url, api_token):
        self.api_url = base_url
        self.api_token = api_token

    def get_event(self, event_id):
        """ Sending a request at the C42 REST API
            to get an event.
        """
        url = self.build_request_event_url(event_id)
        headers = self.build_request_headers()

        response = self.query_C42_REST_API(url, headers)
        if response.status_code != 200:
            raise ValueError('Error; Something went wrong while getting a responce from the C42 server. Starting a bloody war..')

        return response

    def get_event_subscriptions(self, event_id):
        """ Sending a request at the C42 REST API
            to get an the event subscriptions.
        """
        url = self.build_request_event_subscriptions_url(event_id)
        headers = self.build_request_headers()

        response = self.query_C42_REST_API(url, headers)
        if response.status_code != 200:
            raise ValueError('Error; Something went wrong while getting a responce from the C42 server. Starting a bloody war..')

        return response

    def build_request_headers(self):
        header = {'Accept': 'application/json',
                  'Content-type': 'application/json',
                  'Authorization': 'Token {}'.format(self.api_token)}
        return header

    def build_request_event_url(self, event_id):
        return '{}events/{}/'.format(self.api_url, event_id)

    def build_request_event_subscriptions_url(self, event_id):
        return '{}event-subscriptions/?event_ids=[{}]'.format(self.api_url, event_id)

    def query_C42_REST_API(self, url, headers):
        return requests.get(url, headers=headers)

