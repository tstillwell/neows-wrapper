# neows-wrapper

## Python 3 wrapper for NASA NeoWS API ##

Easily explore NASA's Near Earth Object
data collection.

https://api.nasa.gov/api.html#NeoWS


```
import neows-wrapper
neows = neows-wrapper.NEOWebService()
neows.browse()
```
_______________________________________

## API Calls ##

There are three types of lookup supported by the API

Each function can be used by calling it on a NEOWebService instance
with the specified arguments.

example:

```
neows = neows-wrapper.NEOWebService()
neows.feed('2000-01-01', '2001-01-02')
```


__Feed__

`feed(start_date, end_date)`

Accepts two date strings (in 'yyyy-mm-dd' format) and returns a list
of NEOs making their closest approach to Earth during the date
range.

The maximum date range allowed by this function is 7 days.

__Lookup__

`lookup(id)`

Returns a NEO object with the specified id.

__Fetch All__

`fetch_all()`

Returns a list of all NEOs known to the API.
This function is long-running and will be rate-limited
without a valid API key.


## NEO Objects ##

Each function above returns either a NEO object or a list of NEO objects.
These objects represent Near Earth Objects and associated data
available from the webservice.

_______________________________________

Here are the data fields which are provided for each object:

**neo_reference_id**

Unique integer id for each object
This is the SPK-id used to lookup the object

**name**

Name / provisional designation of object

**orbital_data**

Keplerian elements used to calculate and describe
the orbit of the object. Orbital data is not retrieved
when performing 'feed' lookups.

**close_approach_data**

Info on the time and circumstances of the object
making its closest approach to Earth in it's orbit

**hazardous**

Indicates if the object is potentially hazardous. This is
determined by orbit and size classification

*absolute_magnitude_h*

Result of Absolute magnitude(h) calculation-
Observed luminosity/brightness of the object

*estimated_diameter*

Estimated min and max size in various units

*links*

Reference URL for object data in API

_______________________________________

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

### LICENSE ###

MIT license

See LICENSE file for full license text
