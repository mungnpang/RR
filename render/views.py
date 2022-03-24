from django.http import HttpRequest
from django.shortcuts import render

def index_page(request: HttpRequest):
    return render(request, 'main_page.html')

def history_page(request: HttpRequest):
    return render(request, 'history.html')

def repository_page(request: HttpRequest):
    return render(request, 'repository.html')