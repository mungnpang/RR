from pathlib import Path
import os, json

from django.http import request
from repositories.models import repositories
from repositories.apps import RepositoriesConfig as repo
from config.settings import AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import requests

def UPDATE_JSON():
    directory = repo.s3.list_objects_v2(
        Bucket=AWS_STORAGE_BUCKET_NAME,
        Prefix=('archive/')
    )
    json_list = [file['Key'].split('/')[-1].split('.')[0] for file in directory['Contents'][1:]]
    keyword_list = [keyword['keyword'] for keyword in repositories.objects.distinct().values('keyword')]
    not_in_db_list = []
    for file in json_list:
        if file in keyword_list:
            continue
        not_in_db_list.append(file)
    print(not_in_db_list)
    headers = {
        'Authorization': f'AWS {AWS_ACCESS_KEY_ID}:Signature'
    }
    # response = requests.get(url, headers=)
    # test = json.loads(response.text)
    # print(test)
    # BASE_DIR = Path(__file__).resolve().parent.parent.parent
    # path = os.path.join(BASE_DIR, "archive/")
    
    # file_list = os.listdir(path)
    # file_list_py = [file.split('.')[0] for file in file_list]
    # keyword_list = [keyword['keyword'] for keyword in repositories.objects.distinct().values('keyword')]
    # for file in file_list_py:
    #     if file in keyword_list:
    #         continue
    #     with open(path+file, 'r') as f:
    #         json_data = json.load(f)
    #         for repo in json_data:
    #             try:
    #                 repositories.objects.create(
    #                 keyword = file.split('.')[0],
    #                 repo_id = repo['id'],
    #                 repo_name = repo['repo_name'],
    #                 full_name = repo['full_name'],
    #                 description = repo['description'],
    #                 created = repo['created'],
    #                 language = repo['language'],
    #                 stars = repo['stars'],
    #                 forks = repo['forks'],
    #                 subscribers = repo['subscribers'],
    #                 topics = repo['topics']
    #             )
    #             except :
    #                 continue
