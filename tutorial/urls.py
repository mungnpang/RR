from django.urls import path

from . import views

urlpatterns = [

    path("git/tuto/", views.tuto, name="tuto"),
    path("git/", views.git, name="git.html"),
    path("git/<str:name>", views.git_index_click, name="test"),
]

