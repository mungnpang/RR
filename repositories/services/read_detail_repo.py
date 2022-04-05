from repositories.models import Repositories


def read_detail_repo(repo_id: int) -> Repositories:
    return Repositories.objects.get(id=repo_id)
