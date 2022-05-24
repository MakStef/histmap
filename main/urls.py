from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('search/', countries, name='search'),
    re_path(r'^search/(?P<country_slug>[-a0-z9]+)/$', locations),
    re_path(r'^search/(?P<country_slug>[-a0-z9]+)/(?P<location_slug>[-a0-z9]+)/$', history_objects),
    re_path(r'^search/(?P<country_slug>[-a9-z9]+)/(?P<location_slug>[-a0-z9]+)/(?P<history_object_slug>[-a0-z9]+)/$', history_object),
    ]