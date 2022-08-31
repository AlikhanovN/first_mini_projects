from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.
def index(request):
    news = News.objects.all()
    return render(request, "index.html", {"data" : news})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def glasses(request):
    return render(request, "glasses.html")

def shop(request):
    return render(request, "shop.html")
