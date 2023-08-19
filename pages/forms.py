from django import forms
from .models import LaserMarkingParameters

class LaserMarkingParametersForm(forms.ModelForm):
    class Meta:
        model = LaserMarkingParameters
        fields = '__all__'  # Include all fields from the model
