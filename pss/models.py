from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=200,blank=True,null=True)
    last_name=models.CharField(max_length=200,blank=True,null=True)
    middle_name=models.CharField(max_length=200,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profilepic/',blank=True,null=True)
    phone_num=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=1000,blank=True,null=True)
class SchoolModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    study=models.IntegerField()
    telugu=models.IntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    social=models.IntegerField()
    math=models.IntegerField()
    physics=models.IntegerField()
    biology=models.IntegerField()
    pass_yr=models.IntegerField()
    ispass=models.BooleanField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    yr=models.IntegerField()
    sem=models.IntegerField()
    subject=models.CharField(max_length=200)
    marks=models.IntegerField()
class AttendanceModel(models.Model):
    studentid=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=False,default=datetime.datetime.now())
    ispresent=models.BooleanField()
class BtechModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    yr=models.IntegerField()
    sem=models.IntegerField()
    subject=models.CharField(max_length=200)
    marks=models.IntegerField()
class DiplomaModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    yr=models.IntegerField()
    sem=models.IntegerField()
    subject=models.CharField(max_length=200)
    marks=models.IntegerField()

class FeeModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=False,default=datetime.datetime.now())
    particulars=models.CharField(max_length=500)
    amount=models.IntegerField()
    recipt=models.ImageField(upload_to=f'recipts/')

class GroceriesModel(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    unit = models.CharField(max_length=50)
    stock_added_date=models.DateTimeField(auto_now_add=False,default=datetime.datetime.now())






