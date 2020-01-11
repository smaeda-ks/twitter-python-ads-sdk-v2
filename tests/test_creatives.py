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
def test_account_media():
    initialize_responses('account_media', account_id=client.account_id, id='id')

    response = client.account_media('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.account_media('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.account_media('delete', id='id')
    assert responses.calls[2].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_scheduled_tweets():
    initialize_responses('scheduled_tweets', account_id=client.account_id, id='id')

    response = client.scheduled_tweets('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.scheduled_tweets('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.scheduled_tweets('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.scheduled_tweets('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.scheduled_tweets('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_draft_tweets():
    initialize_responses('draft_tweets', account_id=client.account_id, id='id')

    response = client.draft_tweets('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.draft_tweets('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.draft_tweets('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.draft_tweets('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.draft_tweets('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_draft_tweets_preview():
    initialize_responses(
        'draft_tweets_preview',
        resouce_table=RESOURCE_TABLE['draft_tweets_preview']['RESOURCE'],
        endpoint_type='create',
        account_id=client.account_id,
        id='id')

    response = client.draft_tweets_preview('create', draft_tweet_id='id')
    assert responses.calls[0].request.method == METHOD_MAP['create']
    assert response.body == 'create'


@responses.activate
def test_tweets():
    initialize_responses(
        'tweets',
        resouce_table=RESOURCE_TABLE['tweets']['RESOURCE_GET'],
        endpoint_type='all',
        account_id=client.account_id,
    )
    initialize_responses(
        'tweets',
        resouce_table=RESOURCE_TABLE['tweets']['RESOURCE_POST'],
        endpoint_type='create',
        account_id=client.account_id,
    )

    response = client.tweets('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.tweets('create')
    assert responses.calls[1].request.method == METHOD_MAP['create']
    assert response.body == 'create'


@responses.activate
def test_tweet_previews():
    initialize_responses('tweet_previews', account_id=client.account_id)

    response = client.tweet_previews('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'


@responses.activate
def test_image_app_download_cards():
    initialize_responses('image_app_download_cards', account_id=client.account_id, id='id')

    response = client.image_app_download_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.image_app_download_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.image_app_download_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.image_app_download_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.image_app_download_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_image_conversation_cards():
    initialize_responses('image_conversation_cards', account_id=client.account_id, id='id')

    response = client.image_conversation_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.image_conversation_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.image_conversation_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.image_conversation_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.image_conversation_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_video_app_download_cards():
    initialize_responses('video_app_download_cards', account_id=client.account_id, id='id')

    response = client.video_app_download_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.video_app_download_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.video_app_download_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.video_app_download_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.video_app_download_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_video_conversation_cards():
    initialize_responses('video_conversation_cards', account_id=client.account_id, id='id')

    response = client.video_conversation_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.video_conversation_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.video_conversation_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.video_conversation_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.video_conversation_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_video_website_cards():
    initialize_responses('video_website_cards', account_id=client.account_id, id='id')

    response = client.video_website_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.video_website_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.video_website_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.video_website_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.video_website_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_website_cards():
    initialize_responses('website_cards', account_id=client.account_id, id='id')

    response = client.website_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.website_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.website_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.website_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.website_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_image_direct_message_cards():
    initialize_responses('image_direct_message_cards', account_id=client.account_id, id='id')

    response = client.image_direct_message_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.image_direct_message_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.image_direct_message_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.image_direct_message_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.image_direct_message_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_video_direct_message_cards():
    initialize_responses('video_direct_message_cards', account_id=client.account_id, id='id')

    response = client.video_direct_message_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.video_direct_message_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.video_direct_message_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.video_direct_message_cards('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.video_direct_message_cards('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_poll_cards():
    initialize_responses('poll_cards', account_id=client.account_id, id='id')

    response = client.poll_cards('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.poll_cards('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.poll_cards('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.poll_cards('delete', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_cards_fetch():
    initialize_responses('cards_fetch', account_id=client.account_id, id='id')

    response = client.cards_fetch('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.cards_fetch('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'


@responses.activate
def test_media_library():
    initialize_responses('media_library', account_id=client.account_id, id='id')

    response = client.media_library('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.media_library('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.media_library('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.media_library('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.media_library('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'


@responses.activate
def test_preroll_call_to_actions():
    initialize_responses('preroll_call_to_actions', account_id=client.account_id, id='id')

    response = client.preroll_call_to_actions('all')
    assert responses.calls[0].request.method == METHOD_MAP['all']
    assert response.body == 'all'

    response = client.preroll_call_to_actions('load', id='id')
    assert responses.calls[1].request.method == METHOD_MAP['load']
    assert response.body == 'load'

    response = client.preroll_call_to_actions('create')
    assert responses.calls[2].request.method == METHOD_MAP['create']
    assert response.body == 'create'

    response = client.preroll_call_to_actions('update', id='id')
    assert responses.calls[3].request.method == METHOD_MAP['update']
    assert response.body == 'update'

    response = client.preroll_call_to_actions('delete', id='id')
    assert responses.calls[4].request.method == METHOD_MAP['delete']
    assert response.body == 'delete'
