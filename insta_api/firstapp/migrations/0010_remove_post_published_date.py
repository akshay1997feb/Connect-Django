# Generated by Django 2.1 on 2019-03-04 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_auto_20190304_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]