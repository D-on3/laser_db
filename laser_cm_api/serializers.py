from rest_framework import serializers
from laser_color_marking_db.models import LaserMarkingParameters

# The LaserMarkingParametersSerializer class is a serializer for laser marking
# parameters.
class LaserMarkingParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaserMarkingParameters
        fields = '__all__'
# The ColorSearchSerializer class is a serializer for color search
# functionality.


class ColorSearchSerializer(serializers.Serializer):
    hex_color = serializers.CharField(max_length=7)  # Hex color code, e.g., "#RRGGBB"
