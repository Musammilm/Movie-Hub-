# Generated by Django 4.1.7 on 2023-03-09 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_remove_theatre_data_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked_data',
            name='screenshot',
        ),
    ]
