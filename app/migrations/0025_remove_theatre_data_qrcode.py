# Generated by Django 4.1.7 on 2023-03-08 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_addmovies_no_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatre_data',
            name='qrcode',
        ),
    ]