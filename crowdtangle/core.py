"""CrowdTangle API core classes.
"""
import requests as rq
from datetime import datetime, timedelta
import time

class Client():
    '''A client for Facebook CrowdTangle API.
    '''
    def __init__(self, api_key):
        self.api_key = {'token': api_key}
        self.BASE_URL = 'https://api.crowdtangle.com/'
        self.page_params = {'count': 100, 'offset':0}
        self.CALLS_PER_MIN_OVERALL = 6
        self.CALLS_PER_MIN_LINKS = 3 # still not used.
        self.ncalls = 0 # API rate simple limit control.

    def lists(self, types = None):
        '''Retrieve the lists, saved searches and saved post lists of the dashboard associated with the token
        implicit in the client connection.
        '''
        endpoint = self.BASE_URL + 'lists'
        params = {}
        raw = rq.get(endpoint, params={**params, **self.api_key}).json()
        return map(lambda x: CTList(x), 
                    filter(lambda x: types is None or x['type'] in types,
                    raw['result']['lists']))


    def accounts(self, lst):
        '''Retrieve the accounts for a given list. 
          Accounts may only be retrieved for lists of type LIST, 
          as saved searches and saved posts do not have associated accounts.
          params:
          lst: either a CTAccount object or a string with the id of the list. 
 
        '''
        lstid = lst.id if type(lst) is CTList else lst
        endpoint = self.BASE_URL + 'lists/' + str(lstid) + '/accounts'
        params = {}
        return self._generate(endpoint, params, 'accounts', CTAccount) 
    
    def post(self, id):
        '''How to know the id? 
        '''
        endpoint = self.BASE_URL + 'ctpost/' + str(id) 
        params = {}
        raw = rq.get(endpoint, params={**params, **self.api_key}).json()
        return map(lambda x: CTList(x), raw['result']['lists'])

    def posts(self):
        '''Retrieve the accounts for a given list. 
          Accounts may only be retrieved for lists of type LIST, 
          as saved searches and saved posts do not have associated accounts.
          params:
          lst: either a CTAccount object or a string with the id of the list. 
 
        '''
        endpoint = self.BASE_URL + 'posts'
        params = {'startDate': "2020-08-10"}
        return self._generate(endpoint, params, 'posts', CTPost) 
    


    def _generate(self, endpoint, params, rslt_tag, cls):
        ''' Returns a generator for the results of the endpoint with the given parameters
            and the hint on the result tag to be used. 
            NOTE: Could use the pagination feature instead: 
                https://github.com/CrowdTangle/API/wiki/Pagination
        '''
        while True:
            raw = rq.get(endpoint, params={**params, **self.api_key, **self.page_params}).json()
            self.ncalls += 1 
            self.page_params['offset'] +=100    
            #print(raw['result']['pagination']['nextPage'])
            print(raw['status'])
            if not raw['result'][rslt_tag]:
                self.page_params['offset'] = 0
                self.ncalls = 0
                break
            for acc in  map(lambda x: cls(x), raw['result'][rslt_tag]):
                yield acc
            if self.ncalls == self.CALLS_PER_MIN_OVERALL: # Does not work for links by default!
                print('waiting...')
                time.sleep(60)
                self.ncalls = 0


class CTList():
    def __init__(self, entries):
        self.__dict__.update(entries)
    def __repr__(self):
        return 'CTList({})'.format( str(self.__dict__))

class CTAccount():
    def __init__(self, entries):
        self.__dict__.update(entries)
    def __repr__(self):
        return 'CTAccount({})'.format( str(self.__dict__))

class CTPost():
    def __init__(self, entries):
        self.__dict__.update(entries)
    def __repr__(self):
        return 'CTPost({})'.format( str(self.__dict__))
   