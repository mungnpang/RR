from django.http import HttpRequest
from django.shortcuts import render
import requests

def index_page(request: HttpRequest):
    return render(request, 'main_page.html')

def history_page(request: HttpRequest):
    return render(request, 'history.html')

def repository_page(request: HttpRequest):
    return render(request, 'repository.html')

def detail_page(request: HttpRequest, repo_id: int):
    repo = requests.get(f'http://127.0.0.1:8000/api/v1/repository/detail/{repo_id}').json()
    comments = requests.get(f"http://127.0.0.1:8000/api/v1/comment/read/{repo_id}").json()
    replys = requests.get(f"http://127.0.0.1:8000/api/v1/comment/read_reply/{repo_id}").json()
    try:
        comments['message']
    except TypeError:
        return render(request, 'detail.html', {'repo':repo, 'comments':comments, 'replys':replys})
    else:
        return render(request, 'detail.html', {'repo':repo})