import copy
import json
import unittest
import os

import requests_mock
from fitbit import Fitbit


class TestFitbit(unittest.TestCase):
    """class for testing fitbit."""

    client_kwargs = {
        'client_id': os.environ.get('CLIENT_ID', "22CY22"),
        'client_secret': os.environ.get('CLIENT_SECRET',
                                        "25058b02498c0b78ce12249454570331"),
        'redirect_uri': os.environ.get('REDIRECT_URI'),
        'scope': 'weight'
    }

    client_id = os.environ.get('CLIENT_ID', "22CY22")
    client_secret = os.environ.get('CLIENT_SECRET',
                                   "25058b02498c0b78ce12249454570331")
    redirect_uri = os.environ.get('REDIRECT_URI')

    def test_fetch_access_token(self):
        """Tests the fetching of access token using code and redirect_URL."""
        fb = Fitbit(**self.client_kwargs)
        fake_code = "fake_code"
        with requests_mock.mock() as m:
            m.post(fb.client.access_token_url, text=json.dumps({
                'access_token': 'fake_return_access_token',
                'refresh_token': 'fake_return_refresh_token'
            }))
            response = fb.client.fetch_access_token(fake_code)
        self.assertEqual("fake_return_access_token", response['access_token'])
        self.assertEqual(
            "fake_return_refresh_token", response['refresh_token'])

    def test_refresh_token(self):
        """Test of refresh function."""
        kwargs = copy.copy(self.client_kwargs)
        kwargs['access_token'] = 'fake_access_token'
        kwargs['refresh_token'] = 'fake_refresh_token'
        kwargs['refresh_cb'] = lambda x: None
        fb = Fitbit(**kwargs)
        with requests_mock.mock() as m:
            m.post(fb.client.refresh_token_url, text=json.dumps({
                'access_token': 'fake_return_access_token',
                'refresh_token': 'fake_return_refresh_token'
            }))
            response = fb.client.refresh_token()
        self.assertEqual("fake_return_access_token", response['access_token'])
        self.assertEqual(
            "fake_return_refresh_token", response['refresh_token'])


if __name__ == '__main__':
    unittest.main()
