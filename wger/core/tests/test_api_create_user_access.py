# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

import logging

from django.core.urlresolvers import reverse

from wger.core.tests.base_testcase import WorkoutManagerTestCase

logger = logging.getLogger(__name__)


class ApiKeyTestCase(WorkoutManagerTestCase):
    '''
    Tests if user has access
    '''

    def test_api_key_page_shows_user_has_no_access(self):
        '''
        Tests user has access to create users
        '''

        self.user_login('test')

        response = self.client.get(reverse('core:user:api-key'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Pending request to gain access ' + ''
            + 'to create users through api.')

    def test_api_key_page_shows_user_has_access(self):
        '''
        Tests user has requested access but approval.
        '''

        self.user_login('demo')

        response = self.client.get(reverse('core:user:api-key'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'You have access to create users through the api.')

    def test_api_key_page_shows_user_pending_access(self):
        '''
        Tests user has no access to create users
        '''

        self.user_login('trainer1')

        response = self.client.get(reverse('core:user:api-key'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Request for access to add user through api.')
