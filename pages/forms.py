
# forms.py
from django import forms
from .models import LaserSource, Material,LaserMarkingParameters


class GaeParamsForm(forms.Form):
    hex_color = forms.CharField(
        label='Choose a Color',
        max_length=7,
        widget=forms.TextInput(attrs={'type': 'color'}),
    )



class LaserSourceForm(forms.ModelForm):
    class Meta:
        model = LaserSource
        fields = ['name', 'type_of_laser', 'wavelength']


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description']


class AddSampleForm(forms.Form):
    laser_source = forms.ModelChoiceField(queryset=LaserSource.objects.all(),
                                          label='Laser Source')
    material = forms.ModelChoiceField(queryset=Material.objects.all())
    scanning_speed = forms.IntegerField(label='Scanning Speed', min_value=1)
    average_power = forms.DecimalField(label='Average Power', max_digits=5,
                                       decimal_places=2, min_value=0.01)
    scan_step = forms.FloatField(label='Scan Step', required=False)
    pulse_duration = forms.FloatField(label='Pulse Duration', required=False)
    pulse_repetition_rate = forms.IntegerField(label='Pulse Repetition Rate',
                                               required=False, min_value=1)
    focus = forms.FloatField(label='Focus', required=False)
    color_red = forms.IntegerField(label='Color Red', required=False,
                                   min_value=0, max_value=255)
    color_green = forms.IntegerField(label='Color Green', required=False,
                                     min_value=0, max_value=255)
    color_blue = forms.IntegerField(label='Color Blue', required=False,
                                    min_value=0, max_value=255)
    authors = forms.CharField(label='Authors', max_length=100)
    research_date = forms.DateTimeField(label='Research Date',
                                        widget=forms.DateTimeInput(
                                            attrs={'type': 'datetime-local'}))


class LaserMarkingParametersForm(forms.ModelForm):
    class Meta:
        model = LaserMarkingParameters
        fields = '__all__'