import responses
import twitter_ads_v2
from twitter_ads_v2.resources import RESOURCE_TABLE
from helpers import (
    with_resource, with_fixture, characters, initialize_responses, METHOD_MAP)


client = twitter_ads_v2.Client(
    'testaccount',
    characters(40),
    characters(40),
    characters(40),
    characters(40)
)


@responses.activate
def test_active_entities():
    initialize_responses('active_entities', account_id=client.account_id)

    response = client.active_entities('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_analytics_sync_stats():
    initialize_responses('analytics_sync_stats', account_id=client.account_id)

    response = client.analytics_sync_stats('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_analytics_async_jobs():
    initialize_responses('analytics_async_jobs', account_id=client.account_id, id='id')

    response = client.analytics_async_jobs('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.analytics_async_jobs('delete', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_analytics_async_create_job():
    initialize_responses('analytics_async_create_job', account_id=client.account_id, id='id')

    response = client.analytics_async_create_job('create')
    assert responses.calls[0].request.method == METHOD_MAP['create']
    assert response.body == 'create'


@responses.activate
def test_reach_frequency_campaigns():
    initialize_responses('reach_frequency_campaigns', account_id=client.account_id)

    response = client.reach_frequency_campaigns('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_reach_frequency_funding_instruments():
    initialize_responses('reach_frequency_funding_instruments', account_id=client.account_id)

    response = client.reach_frequency_funding_instruments('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'
