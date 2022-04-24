from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    data = {
        'levels' : Level.objects.all(),
    }
    return render(request, "main/index.html", data)