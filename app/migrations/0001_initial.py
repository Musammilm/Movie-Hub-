# Generated by Django 4.1.7 on 2023-02-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='theatre_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('Password', models.CharField(max_length=30, null=True)),
                ('gstno', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('License_No', models.IntegerField(null=True)),
                ('phone', models.IntegerField(null=True)),
                ('Facilities', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('specification', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('Password', models.CharField(max_length=30, null=True)),
                ('Confirm_Password', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('area_code', models.IntegerField(null=True)),
                ('phone', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
