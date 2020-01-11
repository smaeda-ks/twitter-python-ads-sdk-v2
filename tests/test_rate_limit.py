import responses
import time
import twitter_ads_v2
from twitter_ads_v2.resources import RESOURCE_TABLE
from twitter_ads_v2.http import Response
from twitter_ads_v2.error import RateLimit
from helpers import (
    with_resource, with_fixture, characters, initialize_responses, METHOD_MAP)


client1 = twitter_ads_v2.Client(
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

client2 = twitter_ads_v2.Client(
    'testaccount',
    characters(40),
    characters(40),
    characters(40),
    characters(40),
    options={
        'handle_rate_limit': True
    }
)


@responses.activate
def test_rate_limit_handle_with_retry_success_1(monkeypatch):
    # scenario:
    #  - 500 (retry) -> 429 (handle rate limit) -> 200 (end)
    monkeypatch.setattr(time, 'sleep', lambda s: None)

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=500,
        account_id=client1.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=429,
        headers={
            'x-account-rate-limit-limit': '10000',
            'x-account-rate-limit-remaining': '0',
            'x-account-rate-limit-reset': str(int(time.time()) + 5)
        },
        account_id=client1.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=200,
        account_id=client1.account_id,
        id='id'
    )

    response = client1.campaigns('all')

    assert response.body == 'all'
    assert len(responses.calls) == 3
    assert isinstance(response, Response)


@responses.activate
def test_rate_limit_handle_with_retry_success_2(monkeypatch):
    # scenario:
    #  - 429 (handle rate limit) -> 500 (retry) -> 200 (end)
    monkeypatch.setattr(time, 'sleep', lambda s: None)

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=429,
        headers={
            'x-account-rate-limit-limit': '10000',
            'x-account-rate-limit-remaining': '0',
            'x-account-rate-limit-reset': str(int(time.time()) + 5)
        },
        account_id=client1.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=500,
        account_id=client1.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=200,
        account_id=client1.account_id,
        id='id'
    )

    response = client1.campaigns('all')

    assert response.body == 'all'
    assert len(responses.calls) == 3
    assert isinstance(response, Response)


@responses.activate
def test_rate_limit_handle_success(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s: None)

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=429,
        headers={
            'x-account-rate-limit-limit': '10000',
            'x-account-rate-limit-remaining': '0',
            'x-account-rate-limit-reset': str(int(time.time()) + 5)
        },
        account_id=client1.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=200,
        account_id=client1.account_id,
        id='id'
    )

    response = client2.campaigns('all')

    assert response.body == 'all'
    assert len(responses.calls) == 2
    assert isinstance(response, Response)


@responses.activate
def test_rate_limit_handle_error(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s: None)

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=429,
        headers={
            'x-account-rate-limit-limit': '10000',
            'x-account-rate-limit-remaining': '0',
            'x-account-rate-limit-reset': str(int(time.time()) + 5)
        },
        account_id=client1.account_id,
        id='id'
    )

    initialize_responses(
        'campaigns',
        resouce_table=RESOURCE_TABLE['campaigns']['RESOURCE_COLLECTION'],
        endpoint_type='all',
        status=429,
        headers={
            'x-account-rate-limit-limit': '10000',
            'x-account-rate-limit-remaining': '0',
            'x-account-rate-limit-reset': str(int(time.time()) + 5)
        },
        account_id=client1.account_id,
        id='id'
    )

    try:
        response = client2.campaigns('all')
    except Exception as e:
        error = e

    assert len(responses.calls) == 2
    assert isinstance(error, RateLimit)
