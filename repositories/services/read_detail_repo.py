from repositories.models import Repositories

def READ_DETAIL_REPO(repo_id: int)-> Repositories:
    return Repositories.objects.get(id=repo_id)