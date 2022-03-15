from repositories.models import repositories

def READ_DETAIL_REPO(repo_id:str )-> repositories:
    return repositories.objects.get(id=int(repo_id))