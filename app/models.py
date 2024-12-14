from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user_data(models.Model):
    user_name=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    area_code=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    location=models.CharField(max_length=30,null=True)
    gender=models.CharField(max_length=30,null=True)

class theatre_data(models.Model):
    tuser_name=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True)
    gstno=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    License_No=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    Facilities=models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=30,null=True)
    specification=models.CharField(max_length=30,null=True)
    is_active=models.BooleanField(null=True)




class set(models.Model):
    moviename=models.CharField(max_length=30,null=True)
    time=models.CharField(max_length=30,null=True)
    Date=models.DateField(null=True)
    Date1=models.DateField(null=True)
    price=models.IntegerField(null=True)


class booked_data(models.Model):
    theatre = models.ForeignKey(theatre_data,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=30,null=True)
    movie_name = models.CharField(max_length=30,null=True)
    showtime=models.CharField(max_length=30,null=True)
    Date=models.DateField(null=True)
    price_1_tk=models.IntegerField(null=True)
    no_tickets=models.IntegerField(null=True)
    Total_amount=models.IntegerField(null=True)
    seat_no=models.CharField(max_length=30,null=True)

class feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    description = models.TextField(null=True)

class feedbacku(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    description = models.TextField(null=True)


class add_movies(models.Model):
    theatre = models.ForeignKey(theatre_data,on_delete=models.CASCADE)
    movie_name=models.CharField(max_length=30,null=True)
    Director=models.CharField(max_length=30,null=True)
    caste=models.CharField(max_length=30,null=True)
    Category=models.CharField(max_length=30,null=True)
    Language=models.CharField(max_length=30,null=True)
    Date=models.DateField(null=True)
    Date1=models.DateField(null=True)
    set_show=models.CharField(max_length=30,null=True)
    no_tickets=models.IntegerField(null=True)
    no_screen=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(null=True)
    
class payments(models.Model):
    
    name=models.CharField(max_length=30,null=True)
    amount=models.IntegerField(null=True)
    Status=models.CharField(max_length=30,null=True)
    