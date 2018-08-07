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

from rest_framework import serializers
from wger.exercises.models import (
    Muscle,
    Exercise,
    ExerciseImage,
    ExerciseCategory,
    Equipment,
    ExerciseComment
)


class MuscleSerializer(serializers.ModelSerializer):
    '''
    Muscle serializer
    '''

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Muscle

    def get_image_url(self, obj):
        return 'images/muscles/main/muscle-%s.svg' % obj.id


class ExerciseSerializer(serializers.ModelSerializer):
    '''
    Exercise serializer
    '''
    muscles = MuscleSerializer(read_only=True, many=True)
    muscles_secondary = MuscleSerializer(read_only=True, many=True)

    class Meta:
        depth = 2
        model = Exercise



class EquipmentSerializer(serializers.ModelSerializer):
    '''
    Equipment serializer
    '''
    class Meta:
        model = Equipment


class ExerciseCategorySerializer(serializers.ModelSerializer):
    '''
    ExerciseCategory serializer
    '''
    class Meta:
        model = ExerciseCategory


class ExerciseImageSerializer(serializers.ModelSerializer):
    '''
    ExerciseImage serializer
    '''
    class Meta:
        model = ExerciseImage


class ExerciseCommentSerializer(serializers.ModelSerializer):
    '''
    ExerciseComment serializer
    '''
    class Meta:
        model = ExerciseComment
