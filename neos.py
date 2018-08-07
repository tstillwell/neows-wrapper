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
            print response_data
            return NEO(response_data['neo_reference_id'],
                       response_data['name'],
                       orbital_data = response_data['orbital_data'],
                       close_approach_data = response_data['close_approach_data'],
                       potentially_hazerdous = response_data['is_potentially_hazardous_asteroid'],
                       absolute_magnitude = response_data['absolute_magnitude_h'],
                       estimated_diameter = response_data['estimated_diameter'],
                       links = response_data['links']
                      )
        except requests.exceptions.RequestException as e:
            print(e)

    def browse(self):
        """ Browse the overall Asteroid data-set 
            Responses contain a 'next' link to the next page in set """
        endpoint_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse'
        url_params = {'api_key': NASA_API_KEY}
        try:
            browse_query = requests.get(endpoint_url, params=url_params)
            response_data = browse_query.json()
            near_earth_objects = response_data['near_earth_objects']
			neo_list = []
            for neo in near_earth_objects:  # Process each NEO from response
                near_earth_object = NEO(neo['neo_reference_id'], neo['name'])
				neo_list.append(near_earth_object)
            links = response_data['links']
        except requests.exceptions.RequestException as e:
            print(e)
