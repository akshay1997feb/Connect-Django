# Generated by Django 2.1 on 2019-03-06 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_remove_post_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
