from django.contrib import admin
from .models import *
from city.models import City, Navigation


# Register your models here.
admin.site.register(City)
admin.site.register(Navigation)