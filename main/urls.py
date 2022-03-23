from django.urls import path
from main.views import index_page

urlpatterns = [
    path('', index_page, name='main'),
]