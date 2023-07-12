from rest_framework import serializers
from materials.models import Material
from author.models import Author
from machines.models import Machine
from colors.models import ColorOutcome

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class ColorOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorOutcome
        fields = '__all__'
