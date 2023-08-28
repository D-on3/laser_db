from rest_framework import serializers
from pages.models import LaserMarkingParameters

class LaserMarkingParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaserMarkingParameters
        fields = '__all__'


class ColorSearchSerializer(serializers.Serializer):
    hex_color = serializers.CharField(max_length=7)  # Hex color code, e.g., "#RRGGBB"
