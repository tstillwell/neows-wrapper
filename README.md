# neows-wrapper

## Python wrapper for NASA NeoWS API

https://api.nasa.gov/api.html#NeoWS

### Get an API key

If you want to use the API past a few queries, you will need to get a free API key from NASA

Sign up for a NASA API key here

https://api.nasa.gov/index.html#apply-for-an-api-key

To change the API key open `neos.py` and look for the line near the top that has:

`NASA_API_KEY = 'DEMO_KEY'`

Replace DEMO_KEY with your actual API key or your requests will be automatically rate-limited.
