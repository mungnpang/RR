from typing import List
from repositories.models import Repositories

def READ_REPO(keyword: str)-> List[Repositories]:
    return Repositories.objects.filter(keyword=keyword).order_by('-stars')

