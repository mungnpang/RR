from typing import List
from repositories.models import Repositories
from random import random, randrange

def CREATE_REPO_DATA(index: int, keyword: str) -> Repositories:
    return Repositories.objects.create(
            keyword = keyword,
            repo_id = index,
            repo_name = f"repo{index}",
            full_name = f"test/repo{index}",
            description = "testing Repository",
            created = "2022-03-15 17:16",
            language = "python",
            stars = randrange(1,500),
            forks = randrange(1,500),
            subscribers = randrange(1,500),
            topics = ["test","tdd","python","django"]
        )
        
def READ_DETAIL_REPO_DATA(repo_id: int) -> Repositories:
    try:
        repo = Repositories.objects.get(id=repo_id)
    except Repositories.DoesNotExist:
        return "Data is None"
    else:
        return repo

def READ_REPO_DATA(keyword: str) -> List[Repositories]:
    return list(Repositories.objects.filter(keyword=keyword))