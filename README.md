# Getting Started

## Installation

```sh
# install the latest release
pip install twitter-ads-v2
```

## Quick Start

```py
import twitter_ads_v2

CONSUMER_KEY = 'your consumer key'
CONSUMER_SECRET = 'your consumer secret'
ACCESS_TOKEN = 'access token'
ACCESS_TOKEN_SECRET = 'access token secret'
ACCOUNT_ID = 'account id'

client = twitter_ads_v2.Client(
    ACCOUNT_ID,
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    options={
        'handle_rate_limit': True
    }
)

# index
data = client.campaigns('all')
print(data.headers)
print(data.body)

# show
data = client.campaigns('load', id='campaign_id')
print(data.headers)
print(data.body)

tweets = client.promoted_tweets('all')
# iterate over until the cursor ("next_cursor") is exhausted
for i in tweets:
    print(i.headers)
    print(i.body)
```

### Types of `endpoint_type`

To provide a consistent interface, the first parameter of each API method is always `endpoint_type`:

```py
data = client.campaigns('load', id='campaign_id')
```

in the above example, `load` is the `endpoint_type` of this call. The terms of each `endpoint_type` are described below.

|`endpoint_type`|description|HTTP method|
|---|---|---|
| `all` | Retrieve _**all**_ or _**some**_ of the entities’ details depends on the request parameters from an index endpoint (i.e., most index endpoints have a parameter that can scope the results). | GET |
| `load` | Retrieve a _**specific**_ entity details from a show endpoint (i.e., most show endpoints require an entity id to retrieve as part of resource URI). | GET |
| `create` | Create a new entity. | POST |
| `update` | Update a specific entity. | PUT |
| `delete` | Delete a specific entity. | DELETE |
| `batch` | Create/Update/Delete entities depends on the POST body data (normally a JSON object). | POST |

### Request Parameters

All request parameters except `endpoint_type` as mentioned above should be passed as keyword arguments.

### Rate-limit handling and request retry

```py
client = twitter_ads_v2.Client(
    ACCOUNT_ID,
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    options={
        'handle_rate_limit': True,
        'retry_max': 3,
        'retry_delay': 5000,
        'retry_on_status': [404, 500, 503]
    })
```

|parameter|default|description|
|---|:---:|---|
|`handle_rate_limit`|`False` (boolean)|Set `True` will check the rate-limit response header and sleep if the request reached the limit (429).|
|`retry_max`|`0` (int)|The number of times you want to retry when response code is found in `retry_on_status`.|
|`retry_delay`|`1500` (int)|The number of **milliseconds** you want to sleep before retry.|
|`retry_on_status`|`[500, 503]` (list)|The response codes you want to retry on. You can only set >= 400 status codes.|

## Compatibility & Versioning

This project is designed to work with Python 3.5 or greater. While it may work on other versions of Python, below are the platform and runtime versions we officially support and regularly test against.

| Platform | Versions |
| -- | -- |
| CPython | 3.5, 3.6, 3.7 |
| PyPy | 7.x |

All releases adhere to strict semantic versioning. For Example, major.minor.patch-pre (aka. stick.carrot.oops-peek).

## Development

If you’d like to contribute to the project or try an unreleased development version of this project locally, you can do so quite easily by following the examples below.

```sh
# clone the repository
git clone git@github.com:smaeda-ks/twitter-python-ads-sdk-v2.git
cd twitter-python-ads-sdk-v2

# installing a local unsigned release
pip install -e .
```

### Tests

```sh
$ python setup.py flake8 && python setup.py test
```

### Documentation

If you’d like to contribute to the project's documentation, you need to setup Sphinx and build pages by the following steps.

```sh
# install dependencies
$ pip install -e .[doc]

# build pages
$ cd sphinx/
$ make clean && make html
```
