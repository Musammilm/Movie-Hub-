# Generated by Django 4.1.7 on 2023-03-01 20:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_theatre_data1_user_data1_remove_user_data_user_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='theatre_data1',
            new_name='theatre_data',
        ),
        migrations.RenameModel(
            old_name='user_data1',
            new_name='user_data',
        ),
    ]
