from urllib.error import HTTPError
from asgiref.sync import sync_to_async
from config.conf.github_token import token
from repositories.models import repositories
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import asyncio, json
import requests

def db_create(repo_dict: dict, keyword: str, keyword_page:int):
    repositories.objects.create(
        keyword = keyword,
        keyword_page = keyword_page,
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

async def REPO_INFO(repo: str, keyword: str, keyword_page: int) -> None:
    url = 'https://api.github.com/repos/'+repo
    page = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Authorization': f'token {token}'})
    repo_info =  await loop.run_in_executor(None, urlopen, page)
    repo_info =  await loop.run_in_executor(None, repo_info.read)           
    repo_info = json.loads(repo_info.decode())
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
    await sync_to_async(db_create)(repo_dict, keyword, keyword_page)

async def REPO_INFO_CREATE(keyword:str, keyword_page: int) -> None:
    url = f"https://github.com/search?o=desc&p={keyword_page}&q={keyword}&s=stars&type=Repositories"
    # page = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = await loop.run_in_executor(None, requests.get, url)
    # try:
    #     response = await loop.run_in_executor(None, urlopen, page)
    # except HTTPError:
    #     await asyncio.sleep(3)
    #     await REPO_INFO_CREATE(keyword, keyword_page)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.select('#js-pjax-container > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > ul > li > div.mt-n1.flex-auto > div.d-flex > div:nth-child(1) > a')
    if pages == []:
        await asyncio.sleep(5)
        await REPO_INFO_CREATE(keyword, keyword_page)
    for page in pages:
        await REPO_INFO(page.text, keyword, keyword_page)
    print(f"{keyword_page} 작업완료")
    await asyncio.sleep(5)

async def SEARCH(keyword: str):
    pages = [asyncio.ensure_future(REPO_INFO_CREATE(keyword, page)) for page in range(1,4)]
    result = await asyncio.gather(*pages)


@sync_to_async
def MAIN(keyword: str):
    global loop
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as ex:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
    loop.run_until_complete(SEARCH(keyword))
    loop.close()
