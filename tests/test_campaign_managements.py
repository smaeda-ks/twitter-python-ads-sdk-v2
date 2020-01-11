import responses
import twitter_ads_v2
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
def test_accounts():
    initialize_responses('accounts', id='id')

    response = client.accounts('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.accounts('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'


@responses.activate
def test_authenticated_user_access():
    initialize_responses('authenticated_user_access', account_id=client.account_id)

    response = client.authenticated_user_access('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_bidding_rules():
    initialize_responses('bidding_rules')

    response = client.bidding_rules('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_campaigns():
    initialize_responses('campaigns', account_id=client.account_id, id='id')

    response = client.campaigns('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.campaigns('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.campaigns('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.campaigns('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.campaigns('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_content_categories():
    initialize_responses('content_categories')

    response = client.content_categories('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_funding_instruments():
    initialize_responses('funding_instruments', account_id=client.account_id, id='id')

    response = client.funding_instruments('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.funding_instruments('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.funding_instruments('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.funding_instruments('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.funding_instruments('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_iab_categories():
    initialize_responses('iab_categories')

    response = client.iab_categories('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_line_items():
    initialize_responses('line_items', account_id=client.account_id, id='id')

    response = client.line_items('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.line_items('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.line_items('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.line_items('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.line_items('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_line_item_apps():
    initialize_responses('line_item_apps', account_id=client.account_id, id='id')

    response = client.line_item_apps('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.line_item_apps('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.line_item_apps('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.line_item_apps('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_line_item_placements():
    initialize_responses('line_item_placements')

    response = client.line_item_placements('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_media_creatives():
    initialize_responses('media_creatives', account_id=client.account_id, id='id')

    response = client.media_creatives('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.media_creatives('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.media_creatives('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.media_creatives('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_promoted_accounts():
    initialize_responses('promoted_accounts', account_id=client.account_id, id='id')

    response = client.promoted_accounts('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.promoted_accounts('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.promoted_accounts('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.promoted_accounts('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_promoted_tweets():
    initialize_responses('promoted_tweets', account_id=client.account_id, id='id')

    response = client.promoted_tweets('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.promoted_tweets('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.promoted_tweets('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.promoted_tweets('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_promotable_users():
    initialize_responses('promotable_users', account_id=client.account_id, id='id')

    response = client.promotable_users('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.promotable_users('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'


@responses.activate
def test_scheduled_promoted_tweets():
    initialize_responses('scheduled_promoted_tweets', account_id=client.account_id, id='id')

    response = client.scheduled_promoted_tweets('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.scheduled_promoted_tweets('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.scheduled_promoted_tweets('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.scheduled_promoted_tweets('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_targeting_criteria():
    initialize_responses('targeting_criteria', account_id=client.account_id, id='id')

    response = client.targeting_criteria('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.targeting_criteria('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.targeting_criteria('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.targeting_criteria('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_targeting_suggestions():
    initialize_responses('targeting_suggestions', account_id=client.account_id)

    response = client.targeting_suggestions('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_reach_estimate():
    initialize_responses('reach_estimate', account_id=client.account_id)

    response = client.reach_estimate('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_tax_settings():
    initialize_responses('tax_settings', account_id=client.account_id)

    response = client.tax_settings('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.tax_settings('update', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['update']
    assert response.body == 'update'


@responses.activate
def test_user_settings():
    initialize_responses('user_settings', account_id=client.account_id, id='id')

    response = client.user_settings('load', id='id')
    assert responses.calls[0].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.user_settings('update', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['update']
    assert response.body == 'update'


@responses.activate
def test_targeting_criteria_app_store_categories():
    initialize_responses('targeting_criteria_app_store_categories')

    response = client.targeting_criteria_app_store_categories('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_behavior_taxonomies():
    initialize_responses('targeting_criteria_behavior_taxonomies')

    response = client.targeting_criteria_behavior_taxonomies('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_behaviors():
    initialize_responses('targeting_criteria_behaviors')

    response = client.targeting_criteria_behaviors('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_conversations():
    initialize_responses('targeting_criteria_conversations')

    response = client.targeting_criteria_conversations('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_devices():
    initialize_responses('targeting_criteria_devices')

    response = client.targeting_criteria_devices('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_events():
    initialize_responses('targeting_criteria_events')

    response = client.targeting_criteria_events('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_interests():
    initialize_responses('targeting_criteria_interests')

    response = client.targeting_criteria_interests('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_languages():
    initialize_responses('targeting_criteria_languages')

    response = client.targeting_criteria_languages('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_locations():
    initialize_responses('targeting_criteria_locations')

    response = client.targeting_criteria_locations('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_network_operators():
    initialize_responses('targeting_criteria_network_operators')

    response = client.targeting_criteria_network_operators('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_platform_versions():
    initialize_responses('targeting_criteria_platform_versions')

    response = client.targeting_criteria_platform_versions('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_platforms():
    initialize_responses('targeting_criteria_platforms')

    response = client.targeting_criteria_platforms('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_tv_markets():
    initialize_responses('targeting_criteria_tv_markets')

    response = client.targeting_criteria_tv_markets('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_targeting_criteria_tv_shows():
    initialize_responses('targeting_criteria_tv_shows')

    response = client.targeting_criteria_tv_shows('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'
