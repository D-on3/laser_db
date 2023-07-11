
from django import forms
from .models import LaserParameter

class LaserParameterForm(forms.ModelForm):
    class Meta:
        model = LaserParameter
        fields = '__all__'