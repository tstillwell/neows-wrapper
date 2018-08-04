import requests
import time

NASA_API_KEY = 'DEMO_KEY'  # replace DEMO_KEY with your api key


class NEO(object):
    """ Near Earth Object """
    def __init__(self, neo_reference_id, name, **kwargs):
        self.neo_reference_id = neo_reference_id
        self.name = name


class NEOWebService(object):
    """ Webservice API calls see https://api.nasa.gov/api.html#NeoWS """
    def feed(self, start_date, end_date):
        """ Retrieve a list of Asteroids
            based on their closest approach date to Earth 
            Dates expected in format yyyy-mm-dd """
        endpoint_url = 'https://api.nasa.gov/neo/rest/v1/feed'
        url_params = {'start_date': start_date,  
                      'end_date': end_date,
                      'api_key': NASA_API_KEY
                     }
        try:
            feed_query = requests.get(endpoint_url, params=url_params)
            response_data = feed_query.json()
        except requests.exceptions.RequestException as e:
            print(e)

    def lookup(self, neo_reference_id):
        """ Retrieve a specific Asteroid based on its
            NASA JPL small body (SPK-ID) ID """
        endpoint_url = 'https://api.nasa.gov/neo/rest/v1/neo/%s' % neo_reference_id
        url_params = {'api_key': NASA_API_KEY}
        try:
            lookup_query = requests.get(endpoint_url, params=url_params)
            response_data = lookup_query.json()
            return NEO(response_data['neo_reference_id'], response_data['name'],
                       orbital_data = response_data['orbital_data'])
        except requests.exceptions.RequestException as e:
            print(e)

    def browse(self):
        """ Browse the overall Asteroid data-set """
        endpoint_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse'
        url_params = {'api_key': NASA_API_KEY}
        try:
            browse_query = requests.get(endpoint_url, params=url_params)
            response_data = browse_query.json()
        except requests.exceptions.RequestException as e:
            print(e)
