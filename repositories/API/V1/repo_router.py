from typing import List
from django.http import HttpRequest, JsonResponse, response, HttpResponse
from ninja import Router
from repositories.API.V1.schemas import(
    RepoRequest,
    ReadRepoResponse
)
from repositories.services import (
    READ_REPO,
    READ_DETAIL_REPO,
)
from repositories.models import Repositories

router = Router(tags=["repository"])

@router.get("/{keyword}", response=List[ReadRepoResponse])
def Repo_Read(request: HttpRequest, keyword: str) -> List[Repositories]:
    repos = READ_REPO(keyword)
    if type(repos) == str:
        return JsonResponse({"message" : repos}, status=422)
    return list(repos)

@router.get("/detail/{repo}", response=ReadRepoResponse)
def Repo_Read_One(request: HttpRequest, repo: int) -> Repositories:
    repo = READ_DETAIL_REPO(repo)
    if type(repo) == str:
        return JsonResponse({"message" : repo}, status=422)
    return repo