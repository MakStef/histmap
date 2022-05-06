from django.shortcuts import render, get_object_or_404
from .models import *
import random

# Create your views here.
def index(request):
    navigation = Navigation.objects.all()
    random_image =  random.choice(list(Location.objects.all())).image
    context = {
        'navigation' : navigation,
        'random_image' : random_image,
    }
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

def history_object(request, country_slug, location_slug, object_slug):
    navigation = Navigation.objects.all()
    object = History_Object.objects.get(slug=object_slug)
    context = {
        'navigation' : navigation,
        'object' : object,
    }
    return render(request, 'main/object.html', context)