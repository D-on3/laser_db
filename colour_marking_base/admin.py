from django.contrib import admin
from .models import Material, ColorOutcome, Author, Machine, Result

admin.site.register(Material)
admin.site.register(ColorOutcome)
admin.site.register(Author)
admin.site.register(Machine)
admin.site.register(Result)
