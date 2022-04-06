from random import randrange
from typing import List

from repositories.models import Repositories


def create_repo_data(index: int, keyword: str) -> Repositories:
    return Repositories.objects.create(
        keyword=keyword,
        repo_id=index,
        repo_name=f"repo{index}",
        full_name=f"test/repo{index}",
        description="testing Repository",
        created="2022-03-15 17:16",
        language="python",
        stars=randrange(1, 500),
        forks=randrange(1, 500),
        topics=["test", "tdd", "python", "django"],
    )


def read_detail_repo_data(repo_id: int) -> Repositories:
    return Repositories.objects.get(id=repo_id)


def read_repo_data(keyword: str) -> List[Repositories]:
    return list(Repositories.objects.filter(keyword=keyword))
