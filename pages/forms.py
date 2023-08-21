from django import forms
from .models import LaserMarkingParameters , LaserSource

class LaserMarkingParametersForm(forms.ModelForm):
    class Meta:
        model = LaserMarkingParameters
        fields = '__all__'  # Include all fields from the model



class LaserSourceForm(forms.ModelForm):
    class Meta:
        model = LaserSource
        fields = '__all__'