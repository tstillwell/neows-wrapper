"""
neows-wrapper.py
NASA NEOWS API wrapper
MIT LICENSE
https://github.com/tstillwell/neows-wrapper
"""
import requests
import time

# replace DEMO_KEY with your api key
NASA_API_KEY = 'DEMO_KEY'


class NEO(object):
    """ Near Earth Object """
    def __init__(self, neo_reference_id, name, **kwargs):
        self.neo_reference_id = neo_reference_id
        self.name = name
        self.orbital_data = kwargs.pop('orbital_data')
        self.close_approach_data = kwargs.pop('close_approach_data')
        self.hazardous = kwargs.pop('hazardous')
        self.absolute_magnitude = kwargs.pop('absolute_magnitude')
        self.estimated_diameter = kwargs.pop('estimated_diameter')
        self.links = kwargs.pop('links')


class NEOWebService(object):
    """ NASA NEO Webservice API wrapper """
    def populate(self, neo_json):
        """ Make a NEO object with data from API """
        if ('orbital_data' not in neo_json):
            # orbital data is not present in feed() responses
            neo_json['orbital_data'] = []

        return NEO(neo_json['neo_reference_id'],
                   neo_json['name'],
                   orbital_data=neo_json['orbital_data'],
                   close_approach_data=neo_json['close_approach_data'],
                   hazardous=neo_json['is_potentially_hazardous_asteroid'],
                   absolute_magnitude=neo_json['absolute_magnitude_h'],
                   estimated_diameter=neo_json['estimated_diameter'],
                   links=neo_json['links']
                   )

    def processNEOs(self, neos):
        """ Create list of neos using json data from API """
        neo_list = []
        for neo in neos:  # Process each NEO from response
            near_earth_object = self.populate(neo)
            neo_list.append(near_earth_object)
        return neo_list

    def feed(self, start_date, end_date):
        """ Retrieve a list of Asteroids based on
            their closest approach date to Earth
            Dates expected in format yyyy-mm-dd """
        endpoint_url = 'https://api.nasa.gov/neo/rest/v1/feed'
        url_params = {'start_date': start_date,
                      'end_date': end_date,
                      'api_key': NASA_API_KEY
                      }
        try:
            feed_query = requests.get(endpoint_url, params=url_params)
            response_data = feed_query.json()
            neo_list = []
            near_earth_objects = response_data['near_earth_objects']
            # responses contain a day for each date in provided range
            for day in near_earth_objects:
                neos = self.processNEOs(near_earth_objects[day])
                neo_list.extend(neos)
            return neo_list
        except requests.exceptions.RequestException as e:
            print("Error in request. Request: %s. Ex: %s" % feed_query, e)

    def lookup(self, neo_id):
        """ Retrieve a specific Asteroid based on its
            NASA JPL small body (SPK-ID) ID """
        endpoint_url = 'https://api.nasa.gov/neo/rest/v1/neo/%s' % neo_id
        url_params = {'api_key': NASA_API_KEY}
        try:
            lookup_query = requests.get(endpoint_url, params=url_params)
            response_data = lookup_query.json()
            return self.populate(response_data)
        except requests.exceptions.RequestException as e:
            print("Error in request. Request: %s. Ex: %s" % lookup_query, e)

    def browse(self):
        """ Browse the overall Asteroid data-set
            Responses contain a 'next' link to the next page in set """
        endpoint_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse'
        url_params = {'api_key': NASA_API_KEY}
        try:
            browse_query = requests.get(endpoint_url, params=url_params)
            response_data = browse_query.json()
            near_earth_objects = response_data['near_earth_objects']
            neo_list = self.processNEOs(near_earth_objects)
            links = response_data['links']
            return [neo_list, links]
        except requests.exceptions.RequestException as e:
            print("Error in request. Request: %s. Ex: %s" % browse_query, e)

    def fetch_all(self):
        """ Retrieve all Near Earth Objects known to NEOWS API
            CAUTION this operation is long-running
            and fires hundreds of http requests """
        neo_list = []
        initial_page = self.browse()  # Head page with pointer to next page
        neo_list.extend(initial_page[0])
        next_link = initial_page[1]['next']
        pages_remaining = True
        while pages_remaining:
            next_page = requests.get(next_link)
            response_data = next_page.json()
            neos = self.processNEOs(response_data['near_earth_objects'])
            neo_list.extend(neos)
            time.sleep(5)  # pause next request to prevent rate limiting
            if (response_data['links'] and response_data['links']['next']):
                next_link = response_data['links']['next']
            else:  # no more links
                pages_remaining = False
        return neo_list
