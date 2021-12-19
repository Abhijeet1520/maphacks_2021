from django.shortcuts import render
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

def home(request):
    return render(request, 'home.html')


def pollution(request):
    return render(request, 'pollution.html')


def historymap(request):
    return render(request, 'historymap.html')


def travel(request):
    return render(request, 'travel.html')
