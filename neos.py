import requests
import json
import time

NASA_API_KEY = 'DEMO_KEY'  # replace DEOM_KEY with your api key


class NEO(object):
    """ Near Earth Object """
    def __init__(self, name, designation, size_min, size_max)
        self.name = name
        self.designation = designation
        self.distance = distance
        self.size_min = size_min
        self.size_max = size_max


class NEOWebService(object)
    """ Webservice API calls see https://api.nasa.gov/api.html#NeoWS """
    def feed(self, start_date, end_date)
        """ Retrieve a list of Asteroids
            based on their closest approach date to Earth """
        url_params = {'start_date': start_date,
                      'end_date': end_date,
                      'api_key': NASA_API_KEY
                     }
        feed_query = requests.get('https://api.nasa.gov/neo/rest/v1/feed', params=url_params)
        pass
    def lookup(self, asteroid_id)
        """ Retrieve a specific Asteroid based on its
            NASA JPL small body (SPK-ID) ID """
        url_params = {'api_key': NASA_API_KEY}
        lookup_query = results.get('https://api.nasa.gov/neo/rest/v1/neo/%s' % asteroid_id, params=url_params)
        pass
    def browse(self)
        """ Browse the overal Asteroid data-set """
        url_params = {'api_key': NASA_API_KEY}
        browse_query = requests.get('https://api.nasa.gov/neo/rest/v1/browse', params=url_params)
        pass
