import string
import random
import responses

from twitter_ads_v2.resources import RESOURCE_TABLE
from twitter_ads_v2 import API_VERSION


METHOD_MAP = {
    'all': 'GET',
    'load': 'GET',
    'create': 'POST',
    'update': 'PUT',
    'delete': 'DELETE',
    'batch': 'POST'
}


def with_resource(resource):
    return 'https://ads-api.twitter.com{resource}'.format(resource=resource)


def with_fixture(name):
    f = open('tests/fixtures/{name}.json'.format(name=name), 'r')
    return f.read()


def characters(length):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def initialize_responses(
    resource,
    *,
    domain='ads-api.twitter.com',
    resouce_table=None,
    endpoint_type=None,
    status=200,
    headers={},
    **kwargs
):
    endpoint_types = RESOURCE_TABLE[resource]['endpoint_types']

    if resouce_table:
        base = resouce_table
        base_uri = '/' + API_VERSION + '/' + base.format(**kwargs)
        responses.add(
            responses.Response(
                method=METHOD_MAP[endpoint_type],
                url='https://{domain}'.format(domain=domain) + base_uri,
                status=status,
                headers=headers,
                body=endpoint_type
            )
        )
    else:
        for operation in endpoint_types:
            if operation in ['all', 'create']:
                base = RESOURCE_TABLE[resource]['RESOURCE_COLLECTION']
            elif operation in ['load', 'delete', 'update']:
                base = RESOURCE_TABLE[resource]['RESOURCE']

            base_uri = '/' + API_VERSION + '/' + base.format(**kwargs)
            responses.add(
                responses.Response(
                    method=METHOD_MAP[operation],
                    url='https://{domain}'.format(domain=domain) + base_uri,
                    status=status,
                    headers=headers,
                    body=operation
                )
            )
