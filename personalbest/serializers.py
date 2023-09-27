from .models import personalBest
from rest_framework import serializers

class PersonalBestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = personalBest
        fields =('id', 'Cardio', 'Benchpress', 'Deadlift', 'Squat', 'Shoulderpress')