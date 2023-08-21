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
from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
