from django.contrib import admin
from .models import *

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ("name",),
    }
# Register your models here.
admin.site.register(Navigation)
admin.site.register(Country, SlugAdmin)
admin.site.register(Location, SlugAdmin)
admin.site.register(History_Object, SlugAdmin)