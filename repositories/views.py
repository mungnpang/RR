from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def search(request: HttpRequest):
    return render(request, 'repo.html')