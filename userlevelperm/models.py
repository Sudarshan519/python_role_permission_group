from django.db import models
from django.contrib.auth.models import AbstractUser
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
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True,default=5)
      profile_created = models.BooleanField(default=False,null=True) 
      firebase_token=models.CharField(max_length=255,null=True,blank=True)
      created_gps=models.CharField(max_length=255,blank=True,null=True)
      device_id=models.CharField(max_length=255,blank=False,null=False,default='admin')   
 
    #        permissions=()
 
    
         
 
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