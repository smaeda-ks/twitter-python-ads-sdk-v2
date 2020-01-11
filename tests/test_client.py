import twitter_ads_v2
from helpers import characters
from twitter_ads_v2.client import Client


client = twitter_ads_v2.Client(
    'testaccount',
    characters(40),
    characters(40),
    characters(40),
    characters(40),
    options={
        'handle_rate_limit': True,
        'retry_max': 1,
        'retry_delay': 3000,
        'retry_on_status': [500]
    }
)


def test_client_options():

    assert isinstance(client, Client)
    assert isinstance(client.options, dict)
    assert len(client.options) == 4


def test_client_update_attributes():

    assert isinstance(client, Client)
    assert client.account_id == 'testaccount'

    client.account_id = 'updatedaccount'
    assert client.account_id == 'updatedaccount'
