# Generated by Django 4.1.7 on 2023-03-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_theatre_data_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]