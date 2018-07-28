import requests
import json
import time

NASA_API_KEY = 'DEMO_KEY'


class NEO(object):
    """ Near Earth Object """
    def __init__(self, name, designation, size_min, size_max)
        self.name = name
        self.designation = designation
        self.distance = distance
        self.size_min = size_min
        self.size_max = size_max


class NEOWebService(object)
    """ Webservice API calls """
    def feed(self, start_date, end_date)
        """ Retrieve a list of Asteroids
            based on their closest approach date to Earth """
        pass
    def lookup(self)
        """ Retrieve a specific Asteroid based on its
            NASA JPL small body (SPK-ID) ID """
        pass
    def browse(self)
        """ Browse the overal Asteroid data-set """
        pass
