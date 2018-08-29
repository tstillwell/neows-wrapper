# neows-wrapper

## Python 3 wrapper for NASA NeoWS API ##

Easily explore NASA's asteroid REST API

https://api.nasa.gov/api.html#NeoWS


```
import neows-wrapper
neows = neows-wrapper.NEOWebService()
neows.browse()
```

## API Calls ##

There are three types of lookup supported by the API

Each function can be used by calling them on a NEOWebService instance

`feed()`

`browse_all()`

`lookup()`


### Get an API key ###

If you want to use the API past a few queries,
you will need to get a free API key from NASA.

Sign up for your NASA API key here

https://api.nasa.gov/index.html#apply-for-an-api-key

To change the API key used by the wrapper,
open `neows-wrapper.py` and look for
the line near the top that has:

`NASA_API_KEY = 'DEMO_KEY'`

Replace DEMO_KEY with your actual API key or 
your API requests will be rate-limited.
