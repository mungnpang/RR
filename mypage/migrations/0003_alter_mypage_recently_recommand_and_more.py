# Generated by Django 4.0.3 on 2022-03-30 04:18

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_rename_user_id_mypage_user_remove_mypage_repo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypage',
            name='recently_recommand',
            field=django_mysql.models.ListCharField(models.IntegerField(), default=[], max_length=66, size=None),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='recently_visit',
            field=django_mysql.models.ListCharField(models.IntegerField(), default=[], max_length=66, size=None),
        ),
    ]