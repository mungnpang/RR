from os import sync
from asgiref.sync import sync_to_async
from repositories.models import repositories

def SEARCH_KEYWORD(keyword: str) -> str:
    result = repositories.objects.filter(keyword=keyword).exists()
    if not result:
        return "none"
    return "already"