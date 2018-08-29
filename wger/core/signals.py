# -*- coding: utf-8 -*-

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
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.utils import timezone

from wger.core.models import UserProfile, UserCache, UserApi
from wger.utils.helpers import disable_for_loaddata


@disable_for_loaddata
def create_user_profile(sender, instance, created, **kwargs):
    '''
    Every new user gets a profile
    '''
    if created:
        UserProfile.objects.create(user=instance)


@disable_for_loaddata
def create_user_api(sender, instance, created, **kwargs):
    '''
    Every new user is created through the api and useraoi object is created
    '''
    if created:
        UserApi.objects.create(user=instance)


@disable_for_loaddata
def create_user_cache(sender, instance, created, **kwargs):
    '''
    Every new user gets a cache table
    '''
    if created:
        UserCache.objects.create(user=instance)


def set_timezone(sender, user, request, **kwargs):
    tzname = user.userprofile.user_timezone
    if tzname:
            timezone.activate(tzname)


user_logged_in.connect(set_timezone)
post_save.connect(create_user_profile, sender=User)
post_save.connect(create_user_api, sender=User)
post_save.connect(create_user_cache, sender=User)
