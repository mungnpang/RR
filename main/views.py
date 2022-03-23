from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def index_page(request: HttpRequest):
    return render(request, 'main_page.html')