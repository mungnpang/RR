from repositories.models import Repositories

def READ_REPO(keyword: str)-> Repositories:
    return Repositories.objects.filter(keyword=keyword)
