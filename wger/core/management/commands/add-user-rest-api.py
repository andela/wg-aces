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

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''
    Create users through api
    '''

    help = 'This should be able to grant users\
     access when they want to add users through the api'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username', dest='username', required=True,
            help='username',
        )

    def handle(self, *args, **options):
        username = options['username']
        user = User.objects.get(username=username)
        user_profile = user.userprofile
        user_profile.create_users_api = True
        user_profile.save()

        self.stdout.write("{0} has been granted permisson to \
         add users through api.".format(user.username))
