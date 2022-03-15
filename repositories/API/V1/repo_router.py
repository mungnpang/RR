from typing import List
from django.http import HttpRequest, JsonResponse
from ninja import Router
from repositories.API.V1.schemas import(
    SearchRequest,
    SearchResponse
)
from repositories.services import (
    READ_REPO,
    SEARCH_KEYWORD,
    SEARCH,
    READ_DETAIL_REPO
)
from repositories.services import UPDATE_JSON
from repositories.models import Repositories

router = Router(tags=["repository"])

@router.get("/<str:keyword>", response=List[SearchResponse])
def Repo_Read(request: HttpRequest, keyword: str) -> List[Repositories]:
    repos = READ_REPO(keyword)
    return list(repos)

# @router.get("/", response= None)
# def update_json(request: HttpRequest) -> None:
#     UPDATE_JSON()

@router.get("/detail/<str:repo>", response=SearchResponse)
def Repo_Read_One(request: HttpRequest, repo: str) -> Repositories:
    repo = READ_DETAIL_REPO(repo)
    return repo
    

@router.post("/crawling_data", response=None)
def search_to_repo(request: HttpRequest, search_repo_request: SearchRequest) -> None:
    keyword = search_repo_request.KEYWORD
    keyword_page = SEARCH_KEYWORD(keyword)
    if keyword_page == "already":
        return 
    SEARCH(keyword)

