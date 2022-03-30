from django.apps import AppConfig
import boto3
from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME


class RepositoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'repositories'
    s3 = boto3.client(
        's3', 
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='ap-northeast-2'
        )
    language_img_load = s3.list_objects_v2(
        Bucket = AWS_STORAGE_BUCKET_NAME,
        Prefix=('language_image/')
    )
    
    language_img_list = language_img_load['Contents'][1:]
    language_img_list = [i['Key'].split('/')[-1].split('.')[0] for i in language_img_list]
    
