from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('search/', countries, name='search'),
    re_path(r'^search/(?P<country_slug>[-a-z]+)/$', locations),
    re_path(r'^search/(?P<country_slug>[-a-z]+)/(?P<location_slug>[-a-z]+)/$', history_objects),
    re_path(r'^search/(?P<country_slug>[-a-z]+)/(?P<location_slug>[-a-z]+)/(?P<history_object_slug>[-a-z]+)/$', history_object),
    ]