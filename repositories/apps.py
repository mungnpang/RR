from django.apps import AppConfig
import boto3
from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class RepositoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'repositories'
    s3 = boto3.client(
        's3', 
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='ap-northeast-2'
        )