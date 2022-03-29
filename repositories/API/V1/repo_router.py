from typing import List
from django.http import HttpRequest, JsonResponse, response, HttpResponse
from ninja import Router
from repositories.API.V1.schemas import(
    RepoRequest,
    ReadRepoResponse,
    LanguageResponse
)
from repositories.services import (
    READ_REPO,
    READ_DETAIL_REPO,
)
from repositories.models import Repositories
from repositories.apps import RepositoriesConfig
from urllib.parse import quote
import re

router = Router(tags=["repository"])

@router.get("/detail/{repo}", response=ReadRepoResponse)
def Repo_Read_One(request: HttpRequest, repo: int) -> Repositories:
    repo = READ_DETAIL_REPO(repo)
    if type(repo) == str:
        return JsonResponse({"message" : repo}, status=422)
    return repo

@router.get("/language/{lang}", response=LanguageResponse)
def Language_img_Read(request: HttpRequest, lang: str) -> dict:
    img_list = RepositoriesConfig.language_img_list
    if lang in img_list:
        lang = quote(lang, safe='')
        return JsonResponse({"path":f"https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/{lang}.svg"})
    return JsonResponse({"path":"https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/default.svg"})

@router.get("/{keyword}/{index}", response=List[ReadRepoResponse])
def Repo_Read(request: HttpRequest, keyword: str, index: int ) -> List[Repositories]:
    keyword = re.sub('[^a-zA-Z0-9가-힣]','',keyword)
    repos = READ_REPO(keyword)
    if type(repos) == str:
        return JsonResponse({"message" : repos}, status=422)
    return list(repos)[12*index:12*(index+1)]
