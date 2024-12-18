# Generated by Django 4.1.7 on 2023-03-01 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_theatre_data1_theatre_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='addmovies1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=30, null=True)),
                ('Description', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('no_tickets', models.IntegerField(null=True)),
                ('theatre_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.theatre_data')),
            ],
        ),
        migrations.DeleteModel(
            name='addmovies',
        ),
    ]
