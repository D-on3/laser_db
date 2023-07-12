from django import forms
from .models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['author', 'machine', 'material', 'color', 'power',
                  'pulse_duration', 'repetition_rate', 'focus_position']
