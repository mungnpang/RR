import re
from typing import List
from urllib.parse import quote

from django.http import HttpRequest, HttpResponse, JsonResponse, response
from ninja import Router
from ninja.errors import HttpError

from repositories.API.V1.schemas import (LanguageRequest, LanguageResponse,
                                         ReadRepoResponse, RepoRequest)
from repositories.apps import RepositoriesConfig
from repositories.models import Repositories
from repositories.services import read_detail_repo, read_repo

router = Router(tags=["repository"])


@router.get("/detail/{repo}", response=ReadRepoResponse)
def repo_read_one(request: HttpRequest, repo: int) -> Repositories:
    try:
        repo = read_detail_repo(repo)
    except Repositories.DoesNotExist:
        raise HttpError(404, "Repository Not Found.")
    return repo


@router.get("/language/{lang}", response=LanguageResponse)
def language_img_read(request: HttpRequest, lang: str) -> dict:
    img_list = RepositoriesConfig.language_img_list
    if lang in img_list:
        lang = quote(lang, safe="")
        return JsonResponse({"path": f"https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/{lang}.svg"})
    return JsonResponse({"path": "https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/default.svg"})


@router.post("/language_many/", response=List)
def language_imgs_read(request: HttpRequest, language_request: LanguageRequest) -> List:
    language_list = language_request.DATA
    img_list = RepositoriesConfig.language_img_list
    lang_img_list = []
    for lang in language_list:
        if lang in img_list:
            lang = quote(lang, safe="")
            lang_img_list.append(f"https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/{lang}.svg")
        else:
            lang_img_list.append("https://rrproject.s3.ap-northeast-2.amazonaws.com/language_image/default.svg")
    return lang_img_list


@router.get("/{keyword}/{index}", response=List[ReadRepoResponse])
def repo_read(request: HttpRequest, keyword: str, index: int) -> List[Repositories]:
    keyword = re.sub("[^a-zA-Z0-9가-힣-_]", "", keyword)
    repos = read_repo(keyword)
    if len(repos) == 0:
        raise HttpError(404, "Keyword Not Found")
    return list(repos)[12 * index : 12 * (index + 1)]
