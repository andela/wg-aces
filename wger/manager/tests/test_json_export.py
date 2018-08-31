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


class WorkoutJsonExportTestCase(WorkoutManagerTestCase):
    '''
    Test case for the JSON export for workout
    '''

    def export_json(self):
        '''
        Helper function to test the CSV export
        '''
        response = self.client.get(reverse('manager:workout:export-json'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response['Content-Disposition'],
                         'attachment; filename=Workout.json')

    def test_export_json_logged_in(self):
        '''
        Test the JSON export for workout by a logged in user
        '''

        self.user_login('test')
        self.export_json()
