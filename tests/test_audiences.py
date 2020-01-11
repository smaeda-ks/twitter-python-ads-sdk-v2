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
def test_tailored_audiences():
    initialize_responses('tailored_audiences', account_id=client.account_id, id='id')

    response = client.tailored_audiences('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.tailored_audiences('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.tailored_audiences('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.tailored_audiences('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_tailored_audiences_users():
    pass


@responses.activate
def test_tailored_audience_permissions():
    pass


@responses.activate
def test_insights():
    initialize_responses('insights', account_id=client.account_id)

    response = client.insights('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_insights_available_audiences():
    initialize_responses('insights_available_audiences', account_id=client.account_id)

    response = client.insights_available_audiences('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_keyword_insights():
    initialize_responses('keyword_insights')

    response = client.keyword_insights('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'
