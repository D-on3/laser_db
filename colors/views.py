from django.shortcuts import render
from .models import ColorOutcome

def color_list(request):
    colors = ColorOutcome.objects.all()
    return render(request, 'colors/color_list.html', {'colors': colors})