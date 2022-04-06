"""rr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

from bookmark.API.V1 import router as bookmark_router
from comment.API.V1 import router as comment_router
from mypage.API.V1 import router as mypage_router
from repositories.API.V1 import router as repo_router
from user.API.V1 import router as user_router

api = NinjaAPI()
api.add_router("/user/", user_router)
api.add_router("/comment/", comment_router)
api.add_router("/repository/", repo_router)
api.add_router("/bookmark/", bookmark_router)
api.add_router("/mypage", mypage_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
    path("accounts/", include("allauth.urls"), name="accounts"),
    path("", include("render.urls")),
    path("tutorial/", include("tutorial.urls"), name="tutorial"),
]
