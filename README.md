# neows-wrapper

## Python 3 wrapper for NASA NeoWS API ##

Easily explore NASA's asteroid data

https://api.nasa.gov/api.html#NeoWS

`
    import neows-wrapper
	
    neows = neows-wrapper.NEOWebService()
	
    neows.browse()
`

### Get an API key ###

If you want to use the API past a few queries,
you will need to get a free API key from NASA.

Sign up for a NASA API key here

https://api.nasa.gov/index.html#apply-for-an-api-key

To change the API key open `neows-wrapper.py` and look for
the line near the top that has:

`NASA_API_KEY = 'DEMO_KEY'`

Replace DEMO_KEY with your actual API key or 
your API requests will be rate-limited.
