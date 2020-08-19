"""Main module."""
import requests as rq


class Client():

    def __init__(self, api_key):
        self.api_key = {'token': api_key}
        self.BASE_URL = 'https://api.crowdtangle.com/'

    def lists(self, types = None):
        endpoint = self.BASE_URL + 'lists'
        params = {}
        raw = rq.get(endpoint, params={**params, **self.api_key}).json()
        return filter(lambda x: types is None or x['type'] in types, raw['result']['lists'])

    def accounts(lst):
        pass

class List():
    pass
