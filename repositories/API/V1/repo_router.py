from typing import List
from urllib.error import HTTPError
from django.http import HttpRequest, JsonResponse, response, HttpResponse
from ninja import Router
from render.templatetags.tags import language_list
from repositories.API.V1.schemas import(
    RepoRequest,
    LanguageRequest,
    ReadRepoResponse,
    LanguageResponse
)
from repositories.services import (
    read_repo,
    read_detail_repo,
)
from repositories.models import Repositories
from repositories.apps import RepositoriesConfig
from urllib.parse import quote
import re

router = Router(tags=["repository"])

@router.get("/detail/{repo}", response=ReadRepoResponse)
def repo_read_one(request: HttpRequest, repo: int) -> Repositories:
    try:
        repo = read_detail_repo(repo)
    except Repositories.DoesNotExist:
        raise HTTPError(404, f"Repository #{repo} Not Found.")
    return repo

@router.get("/language/{lang}", response=LanguageResponse)
def language_img_read(request: HttpRequest, lang: str) -> dict:
    img_list = RepositoriesConfig.language_img_list
    if lang in img_list:
        lang = quote(lang, safe='')
        return JsonResponse({"path":f"https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/{lang}.svg"})
    return JsonResponse({"path":"https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/default.svg"})

@router.post("/language_many/", response=List)
def language_imgs_read(request: HttpRequest, language_request: LanguageRequest) -> List:
    language_list = language_request.DATA.split(',')
    img_list = RepositoriesConfig.language_img_list
    lang_img_list = []
    for lang in language_list:
        if lang in img_list:
            lang = quote(lang, safe='')
            lang_img_list.append(f"https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/{lang}.svg")
        else:
            lang_img_list.append("https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/default.svg")
    return lang_img_list

@router.get("/{keyword}/{index}", response=List[ReadRepoResponse])
def repo_read(request: HttpRequest, keyword: str, index: int ) -> List[Repositories]:
    keyword = re.sub('[^a-zA-Z0-9가-힣]','',keyword)
    repos = read_repo(keyword)
    if not len(repos):
        raise HTTPError(404, f"Keyword #{keyword} Not Found")
    return list(repos)[12*index:12*(index+1)]
