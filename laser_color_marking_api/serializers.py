# serializers.py
from rest_framework import serializers
from pages.models import LaserSource, LaserMarkingParameters

class LaserSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaserSource
        fields = '__all__'

class LaserMarkingParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaserMarkingParameters
        fields = '__all__'
