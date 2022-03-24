from django.urls import path
from render.views import index_page, history_page, repository_page

urlpatterns = [
    path('', index_page, name='main'),
    path('history/', history_page, name="history"),
    path('repository/', repository_page, name="repository"),
]