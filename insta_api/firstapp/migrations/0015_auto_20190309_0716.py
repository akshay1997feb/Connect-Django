# Generated by Django 2.1 on 2019-03-09 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_post_post_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_pic',
            new_name='post_pics',
        ),
    ]
