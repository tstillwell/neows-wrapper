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

Accepts two dates in yyyy-mm-dd format and returns a list
of NEOs making their closest approach to Earth during the date
range.

`lookup()`

Returns a NEO object with the specified id.

`browse_all()`

Returns a list of all NEOs known to the API.
This function is long-running and will be rate-limited
without a valid API key.


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
