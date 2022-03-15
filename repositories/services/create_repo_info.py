from config.conf.github_token import token
from repositories.models import Repositories
from bs4 import BeautifulSoup
import requests
from time import sleep
from django.db.utils import IntegrityError

def db_create(repo_dict: dict, keyword: str):
    try:
        Repositories.objects.create(
        keyword = keyword,
        repo_id = repo_dict['id'],
        repo_name = repo_dict['repo_name'],
        full_name = repo_dict['full_name'],
        description = repo_dict['description'],
        created = repo_dict['created'],
        language = repo_dict['language'],
        stars = repo_dict['stars'],
        forks = repo_dict['forks'],
        subscribers = repo_dict['subscribers'],
        topics = repo_dict['topics']
    ) 
    except IntegrityError:
        return

def REPO_INFO(repo: str, keyword: str) -> None:
    url = 'https://api.github.com/repos/'+repo
    repo_info = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Authorization': f'token {token}'}).json()
    repo_dict = {
        'id' : int(repo_info['id']),
        'repo_name' : str(repo_info['name']),
        'full_name' : str(repo_info['full_name']),
        'description' : str(repo_info['description']),
        'created' : str(repo_info['created_at'].replace("T"," ").replace("Z","")),
        'language' : str(repo_info['language']),
        'stars' : int(repo_info['stargazers_count']),
        'forks' : int(repo_info['forks']),
        'subscribers' : int(repo_info['subscribers_count']),
        'topics' : repo_info['topics']
    }
    db_create(repo_dict, keyword)


def REPO_INFO_CREATE(keyword:str, keyword_page: int) -> None:
    url = f"https://github.com/search?o=desc&p={keyword_page}&q={keyword}&s=stars&type=Repositories"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Authorization': f'token {token}'})
    if 'Whoa there!' in response.text:
        sleep(5)
        REPO_INFO_CREATE(keyword, keyword_page)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.select('#js-pjax-container > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > ul > li > div.mt-n1.flex-auto > div.d-flex > div:nth-child(1) > a')

    for page in pages:
        REPO_INFO(page.text, keyword)

def SEARCH(keyword: str):
    pages = [REPO_INFO_CREATE(keyword, page) for page in range(1,31)]


