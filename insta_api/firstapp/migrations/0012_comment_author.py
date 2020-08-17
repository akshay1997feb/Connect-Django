# Generated by Django 2.1 on 2019-03-06 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0011_remove_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
