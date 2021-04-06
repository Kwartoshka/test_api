import pytest
from api import new_folder

request_url = 'https://cloud-api.yandex.net/v1/disk/resources'

with open('token.txt') as f:
    ya_token = f.readline()

variables = ([request_url, ya_token, 'basic', '<Response [201]>'],
             [request_url, ya_token, 'basic', '<Response [409]>'],
             [request_url, '', 'basic', '<Response [401]>'],
             [request_url, ya_token, '', '<Response [400]>'],
             ['https://cloud-api.yandex.net/v1/disk/notfoundpage', ya_token, '', '<Response [40213213]>']
             )


class TestApi:

    @pytest.mark.parametrize('url, token, path, expected', variables)
    def test_new_folder(self, url, token, path, expected):
        assert new_folder(url, token, path) == expected
