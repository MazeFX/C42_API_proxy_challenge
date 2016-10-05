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

    def build_request_headers(self):
        header = {'Accept': 'application/json',
                  'Content-type': 'application/json',
                  'Authorization': 'Token {}'.format(self.api_token)}
        return header

