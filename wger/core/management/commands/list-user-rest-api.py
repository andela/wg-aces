# -*- coding: utf-8 *-*

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

from django.core.management.base import BaseCommand

from wger.core.models import UserApi


class Command(BaseCommand):
    '''
    Get emails of users created through the api
    '''

    help = 'This should be able to get users created through api'

    def handle(self, **options):
        '''
        Process the options
        '''

        self.stdout.write("Users created through api")
        for user in UserApi.objects.all():
            self.stdout.write("{0}".format(user.user.username))
