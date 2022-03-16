from repositories.models import Repositories
from asgiref.sync import sync_to_async

def SEARCH_KEYWORD(keyword: str) -> str:
    result = Repositories.objects.filter(keyword=keyword).exists()
    if not result:
        return "none"
    return "already"