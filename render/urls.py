from django.urls import path

from render.views import (detail_page, history_page, index_page, my_page,
                          nickname, profile_page, repository_page)

urlpatterns = [
    path("", index_page, name="main"),
    path("history/", history_page, name="history"),
    path("repository/", repository_page, name="repository"),
    path("detail/<int:repo_id>", detail_page, name="detail"),
    path("mypage/", my_page, name="mypage"),
    path("mypage/edit_profile", profile_page, name="profile"),
    path("mypage/nickname", nickname, name="nickname"),
]
