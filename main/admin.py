from django.contrib import admin
from .models import *

class ListItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ("name",),
    }
# Register your models here.
admin.site.register(Navigation)
admin.site.register(Country, ListItemAdmin)
admin.site.register(Location, ListItemAdmin)
admin.site.register(History_Object, ListItemAdmin)