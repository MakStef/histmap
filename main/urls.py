from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('map', histmap, name="map")

]