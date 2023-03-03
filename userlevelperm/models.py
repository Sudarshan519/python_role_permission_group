from django.db import models
from django.contrib.auth.models import AbstractUser
from pydantic import validate_email
from django.utils.html import mark_safe
from rest_framework import serializers
from django.contrib.auth.models import Group
class User(AbstractUser):
    DOCTOR = 1
    NURSE = 2
    SURGEN =3
    ADIMN =4
    USER =5
    RESIDENCE=6
    FOREIGNER=7
    ROLE_CHOICES = (
      #   (DOCTOR, 'Doctor'),
      #   (NURSE, 'Nurse'),
      #   (SURGEN, 'Surgen'),
        (RESIDENCE, 'Residence'),(FOREIGNER, 'Foreigner'),
    )
    ACCOUNT_CHOICES=((1,'Individual'),(2,'Business'))
    title=models.PositiveBigIntegerField(choices=((1,'Mr'),(2,'Mrs')),default=1)
    first_name=models.CharField(max_length=255,null=False,blank=False)
    middle_name=models.CharField(max_length=255,null=True,blank=True)
    country=models.CharField(max_length=255,null=True,blank=True)

    # password=models.CharField(max_length=255,blank=False,null=False)
    account_type=models.PositiveBigIntegerField(choices=ACCOUNT_CHOICES,blank=False,null=False,default=1)
    email=models.EmailField(unique=True,validators=[])
    email_verified=models.BooleanField(default=False)
    username=models.CharField(max_length=255,blank=True,null=True,unique=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True,default=5)
    profile_created = models.BooleanField(default=False,null=True) 
    firebase_token=models.CharField(max_length=255,null=True,blank=True)
    created_gps=models.CharField(max_length=255,blank=True,null=True)
    device_id=models.CharField(max_length=255,blank=True,null=True)   
    class Meta:
       permissions=()

       
 

# class EKYCProfile(models.Model):
#     front=models.ImageField(upload_to='media')
#     back=models.ImageField(upload_to='media')
#     selfie=models.ImageField(upload_to='media')
#     liveliness=models.ImageField(upload_to= 'media')
# #
#  class SignUpInfo(models.Model):
    
 
class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    author=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_created=True)

    class Meta:
        permissions = [
            (
                "set_published_status",
                "Can set the status of the post to either publish or not"
            )
        ]
class ResidenceStatus(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    # errorMsg=models.CharField(max_length=255,default='')
    # titlejp=models.CharField(max_length=255,null=False,blank=False)
    # profession=models.ForeignKey(Profession,on_delete=models.Aggregate,null=True)
    def __str__(self) -> str:
        return self.title


class Profession(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True,unique=True)
    residenceStatus=models.ForeignKey(ResidenceStatus,on_delete=models.CASCADE,null=True)
    # titlejp=models.CharField(max_length=255,null=False,blank=False)
    def __str__(self) -> str:
        return self.title


class ApiErrorLog(models.Model):

    platform=models.PositiveBigIntegerField(choices=((0,'Android'),(1,'Ios')),default=1)
    label=models.CharField(max_length=255,default='')
    created_at=models.DateTimeField(auto_now=True)
    log=models.CharField(max_length=255,default='')
    errorMsg=models.CharField(max_length=255,default='')
    funcName=models.CharField(max_length=255,default='')
    device_id=models.CharField(max_length=255,default='')
    def __str__(self) -> str:
        return self.created_at
class Banners(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='media',default='info.png')
    active=models.BooleanField(default=True)
    # def __str__(self) -> str:
    #     return "<img src={self.image}"
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = self.image.url
         ))
class Pages(models.Model):
    title=models.CharField(max_length=255,)
    desc=models.CharField(max_length=255)
    image=models.ImageField(upload_to='media')

class WelcomePages(models.Model):
    pages=models.ForeignKey(Pages,on_delete=models.Aggregate)




