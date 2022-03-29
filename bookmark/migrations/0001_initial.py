# Generated by Django 4.0.3 on 2022-03-28 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repositories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositories.repositories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bookmark',
            },
        ),
        migrations.AddConstraint(
            model_name='bookmark',
            constraint=models.UniqueConstraint(fields=('user', 'repo'), name='unique_user_repo'),
        ),
    ]
