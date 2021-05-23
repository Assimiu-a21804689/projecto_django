from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(request):
    return render(request, "website/home.html")

def base_page_view(request):
    return render(request, "website/base.html")

def filho_page_view(request):
    return render (request, "website/filho1.html")