from django import forms
from .models import Author, Machine, Result

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'year']

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['manufacturer', 'model', 'type']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['author', 'machine', 'color', 'marking_speed', 'power']
