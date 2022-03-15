from repositories.models import repositories
from django.db.models import QuerySet

def READ_REPO(keyword: str)-> QuerySet[repositories]:
    return repositories.objects.filter(keyword=keyword)
