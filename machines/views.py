from django.shortcuts import render
from .models import Machine

def machine_list(request):
    machines = Machine.objects.all()
    return render(request, 'machines/machine_list.html', {'machines': machines})
