# This file is part of wger Workout Manager.

# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU Affero General Public License


from django.contrib.auth.models import User
from rest_framework.test import (
    APITestCase,
    APIClient
)
from rest_framework.authtoken.models import Token
from wger.core.tests.base_testcase import WorkoutManagerTestCase


class ApiCreateUserApi(APITestCase, WorkoutManagerTestCase):
    def test_create_user_through_api(self):
        user = User.objects.get(username='demo')
        token = Token.objects.get(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        data = {
            'username': 'Ronald',
            'password': '12345',
            'email': 'ronald@gmail.com'
        }
        response = client.post('/api/v2/user/', data=data, format='json')
        assert response.status_code == 201

    def test_get_users_through_api(self):
        client = APIClient()
        response = client.get('/api/v2/user/')
        assert response.status_code == 200

    def test_doesnt_create_user_through_api_unauthenticated(self):
        client = APIClient()
        data = {
            'username': 'Ronald',
            'password': '12345',
            'email': 'ronald@gmail.com'
        }
        response = client.post('/api/v2/user/', data=data, format='json')
        assert response.status_code == 403

    def test_doesnt_create_user_through_api_unauthorized_creator(self):
        user = User.objects.get(username='test')
        token = Token.objects.get(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        data = {
            'username': 'Ronald',
            'password': '12345',
            'email': 'ronald@gmail.com'
        }
        response = client.post('/api/v2/user/', data=data, format='json')
        assert response.status_code == 403
