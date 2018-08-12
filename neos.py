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
    def populate(self, neo_json):
        """ Make a NEO object with data from API """
        return NEO(neo_json['neo_reference_id'],
                   neo_json['name'],
                   orbital_data = neo_json['orbital_data'],
                   close_approach_data = neo_json['close_approach_data'],
                   potentially_hazerdous = neo_json['is_potentially_hazardous_asteroid'],
                   absolute_magnitude = neo_json['absolute_magnitude_h'],
                   estimated_diameter = neo_json['estimated_diameter'],
                   links = neo_json['links']
                  )

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
            near_earth_objects = response_data['near_earth_objects']
            neo_list = []
            for neo in near_earth_objects:  # Process each NEO from response
                near_earth_object = populate(neo)
                neo_list.append(near_earth_object)
            return neo_list
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
            return populate(response_data)
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
                near_earth_object = populate(neo)
                neo_list.append(near_earth_object)
            links = response_data['links']
            return [neo_list, links]
        except requests.exceptions.RequestException as e:
            print(e)
            
    def browse_all(self):
    """ Retrieve all Near Earth Objects known to NEOWS API 
        CAUTION this operation is long-running
        and fires hundreds of http requests """
        neo_list = []
        initial_page = browse()  # Head page with pointer to next page
        neo_list.append(initial_page[0])
        next_link = initial_page[1]['next']
        pages_remaining = True
        while pages_remaining:
            