from django.contrib import admin
from .models import *

class CityAdmin (admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('name',)
    }

# Register your models here.
#admin.site.register()