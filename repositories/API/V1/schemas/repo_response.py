from typing import List, Optional
from ninja import Schema

class SearchResponse(Schema):
    keyword: str
    repo_id: int 
    repo_name: str
    full_name: str
    description: Optional[str]
    created: str
    language: str
    stars: int
    forks: int
    subscribers: int
    topics: List