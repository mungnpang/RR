from django.urls import path
from repositories.views import search

urlpatterns =[
    path('', search),
]