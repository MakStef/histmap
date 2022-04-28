from django.shortcuts import render, get_object_or_404
from .models import *
from city.models import City, Navigation
import random

# Create your views here.
def index(request):
    data = {
        'random_image' : (random.choice(list(City.objects.all()))).image,
        'navigation' : Navigation.objects.all(),
    }
    return render(request, "main/index.html", data)