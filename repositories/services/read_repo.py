from typing import List
from repositories.models import Repositories

def READ_REPO(keyword: str)-> List[Repositories]:
    repos = Repositories.objects.filter(keyword=keyword).order_by('-stars')
    if len(repos):
        return repos
    return "Keyword is Empty"
