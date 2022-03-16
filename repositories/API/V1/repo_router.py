from typing import List
from django.http import HttpRequest, JsonResponse, response, HttpResponse
from ninja import Router
from repositories.API.V1.schemas import(
    RepoRequest,
    RepoResponse,
    ReadRepoResponse
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

@router.get("/{keyword}", response=List[ReadRepoResponse])
def Repo_Read(request: HttpRequest, keyword: str) -> List[Repositories]:
    repos = READ_REPO(keyword)
    if type(repos) == str:
        return JsonResponse({"message" : repos}, status=422)
    return list(repos)

# @router.get("/", response= None)
# def update_json(request: HttpRequest) -> None:
#     UPDATE_JSON()

@router.get("/detail/{repo}", response=ReadRepoResponse)
def Repo_Read_One(request: HttpRequest, repo: int) -> Repositories:
    repo = READ_DETAIL_REPO(repo)
    if type(repo) == str:
        return JsonResponse({"message" : repo}, status=422)
    return repo
    
@router.post("/crawling_data/", response=RepoResponse)
def search_to_repo(request: HttpRequest, search_repo_request: RepoRequest) -> dict:
    keyword = search_repo_request.KEYWORD
    keyword_page =  SEARCH_KEYWORD(keyword)
    if keyword_page == "already":
        return JsonResponse({"message" : keyword_page})
    result = SEARCH(keyword)
    return JsonResponse({"message":result})

