from repositories.models import Repositories

def READ_DETAIL_REPO(repo_id: int)-> Repositories:
    try:
        repo = Repositories.objects.get(id=repo_id)
    except Repositories.DoesNotExist:
        return "Repository is None"
    return repo