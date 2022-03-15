from repositories.models import Repositories

def READ_DETAIL_REPO(repo_id:str )-> Repositories:
    return Repositories.objects.get(id=int(repo_id))