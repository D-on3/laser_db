from django.shortcuts import render
from .models import Material

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})
