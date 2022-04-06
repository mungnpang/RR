from typing import List

from repositories.models import Repositories


def read_repo(keyword: str) -> List[Repositories]:
    return Repositories.objects.filter(keyword=keyword).order_by("-stars")
