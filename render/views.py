from django.http import HttpRequest
from django.shortcuts import redirect, render
import requests
from repositories.models import Repositories
from user.models import UserModel
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from user.models import UserModel


def visit_count_check(user_id):
    if user_id:
        user = UserModel.objects.get(id=user_id)
        now = datetime.datetime.now()
        user_last_visit = user.last_visit
        time = now - user_last_visit
        if 'days' not in str(time) and 'day' not in str(time):
            time_hour = list(map(int, str(time).split('.')[0].split(':')))
            if time_hour[0] == 0 and time_hour[1] < 30:
                return
        user.visit_count += 1
        user.last_visit = now
        user.save()
    return


def index_page(request: HttpRequest):
    visit_count_check(request.user.id)
    return render(request, 'main_page.html')


def history_page(request: HttpRequest):
    visit_count_check(request.user.id)
    return render(request, 'history.html')


def repository_page(request: HttpRequest):
    visit_count_check(request.user.id)
    return render(request, 'repository.html')


@login_required(login_url="/accounts/login")
def my_page(request: HttpRequest):
    user = request.user.id
    visit_count_check(user)
    user_data = UserModel.objects.get(id=user)
    bookmark_data = requests.get(f"https://gitlini.com/api/v1/bookmark/read/{user}").json()
    comment_data = requests.get(f"https://gitlini.com/api/v1/comment/read_user/{user}").json()
    history = requests.get(f"https://gitlini.com/api/v1/mypage/read/{user}").json()
    total = set(history['repo_history'] + history['reco_history'])
    repos = list(Repositories.objects.filter(id__in=total))
    repo_data = [0 for _ in range(len(history['repo_history']))]
    reco_data = [0 for _ in range(len(history['reco_history']))]
    for repo in repos:
        if repo.id in history['repo_history']:
            repo_data[history['repo_history'].index(repo.id)] = repo
        if repo.id in history['reco_history']:
            reco_data[history['reco_history'].index(repo.id)] = repo

    return render(request, 'mypage.html', {'user_data': user_data, 'repo_data': repo_data[::-1], 'reco_data': reco_data,
                                           'bookmark_data': bookmark_data, 'comment_data': comment_data})


def detail_page(request: HttpRequest, repo_id: int):
    visit_count_check(request.user.id)
    repo = requests.get(f'https://gitlini.com/api/v1/repository/detail/{repo_id}').json()
    comments = requests.get(f"https://gitlini.com/api/v1/comment/read/{repo_id}").json()
    replys = requests.get(f"https://gitlini.com/api/v1/comment/read_reply/{repo_id}").json()
    try:
        comments['message']
    except TypeError:
        return render(request, 'detail.html', {'repo': repo, 'comments': comments, 'replys': replys})
    else:
        return render(request, 'detail.html', {'repo': repo})


@login_required
def profile_page(request: HttpRequest):
    visit_count_check(request.user.id)
    if request.method == 'POST':
        origin_password = request.POST.get("origin_password")
        user = request.user
        if check_password(origin_password, user.password):
            new_password = request.POST.get("password1")
            user.set_password(new_password)
            user.save()
            return redirect("account_logout")
        else:
            print('error')
            error = {'message': "등록되어있는 비밀번호와 다릅니다."}
            return render(request, 'account/edit_profile.html', {'error': error})
    else:
        return render(request, 'account/edit_profile.html')


@login_required
def nickname(request: HttpRequest):
    if request.method == 'POST':
        nickname = request.POST.get("username")
        user = request.user
        user.username = nickname
        user.save()
        return redirect('mypage')