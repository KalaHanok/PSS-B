from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    first_name=models.CharField(max_length=200,blank=True,null=True)
    last_name=models.CharField(max_length=200,blank=True,null=True)
    middle_name=models.CharField(max_length=200,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profilepic/')
