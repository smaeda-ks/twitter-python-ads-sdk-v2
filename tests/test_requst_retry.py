import responses
import time
import twitter_ads_v2
from twitter_ads_v2.resources import RESOURCE_TABLE
from twitter_ads_v2.http import Response
from twitter_ads_v2.error import NotFound
from helpers import (
    with_resource, with_fixture, characters, initialize_responses, METHOD_MAP)


client = twitter_ads_v2.Client(
    'testaccount',
    characters(40),
    characters(40),
    characters(40),
    characters(40),
    options={
        'retry_max': 1,
        'retry_delay': 3000,
        'retry_on_status': [404, 500, 503]
    }
)


@responses.activate
def test_retry_count_success(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s: None)

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=404,
        account_id=client.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=200,
        account_id=client.account_id,
        id='id'
    )

    response = client.campaigns('all')

    assert response.body == 'all'
    assert len(responses.calls) == 2
    assert isinstance(response, Response)


@responses.activate
def test_retry_count_error(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s: None)

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=404,
        account_id=client.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=404,
        account_id=client.account_id,
        id='id'
    )

    try:
        response = client.campaigns('all')
    except Exception as e:
        error = e

    assert len(responses.calls) == 2
    assert isinstance(error, NotFound)
