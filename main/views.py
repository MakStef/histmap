from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .utils.utils import unzip, path_to_files

from .models import *
from random import choice

# Create your views here.
def index(request):
    navigation = Navigation.objects.all()
    context = {
        'navigation' : navigation,
        'is_image_random': False,
        'image' : None,
    }
    if len(Location.objects.all()) != 0:
        context['is_image_random'] = True
        context['image'] = (choice(list(Location.objects.all()))).image
    else:
        context['is_image_random'] = False
    return render(request, "main/index.html", context)

def countries(request):
    navigation = Navigation.objects.all()
    countries = Country.objects.all()
    context = {
        'navigation' : navigation,
        'items' : countries,
        'currentUrl' : request.get_host(),
    }
    return render(request, 'main/search.html', context)

def locations(request, country_slug):
    navigation = Navigation.objects.all()
    country = get_object_or_404(Country, slug=country_slug)
    locations_list = Location.objects.filter(country=country)
    context = {
        'navigation' : navigation,
        'items' : locations_list,
        'currentUrl' : request.get_host(),
    }
    return render(request, 'main/search.html', context)

def history_objects(request, country_slug, location_slug):
    navigation = Navigation.objects.all()
    location = Location.objects.get(slug=location_slug)
    hist_objects = History_Object.objects.filter(location=location)
    context = {
        'navigation' : navigation,
        'items' : hist_objects,
        'currentUrl' : request.get_host(),
    }
    return render(request, 'main/search.html', context)

def history_object(request, country_slug, location_slug, history_object_slug):
    # Unwraps all archived levels that weren't unwrapped already
    unzip(history_object_slug)
    wasm, data, framework, loader = path_to_files(history_object_slug)
    navigation = Navigation.objects.all()
    object = History_Object.objects.get(slug=history_object_slug)
    context = {
        'navigation' : navigation,
        'object' : object,
        'wasm' : wasm,
        'data' : data,
        'framework' : framework,
        'loader' : loader,
    }
    return render(request, 'main/object.html', context)