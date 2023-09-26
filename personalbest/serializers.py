from .models import personalBest
from rest_framework import serializers

class PersonalBest(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = personalBest
        fields =('id', 'cardio', 'Bench Press', 'Deadlift', 'Squat', 'Shoulder press')