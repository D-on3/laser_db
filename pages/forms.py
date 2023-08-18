from django import forms
from .models import LaserMarkingParameters, LaserColorMarking

class LaserMarkingForm(forms.ModelForm):
    class Meta:
        model = LaserMarkingParameters
        fields = '__all__'  # You can customize which fields to include