from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
      DOCTOR = 1
      NURSE = 2
      SURGEN =3
      
      ROLE_CHOICES = (
          (DOCTOR, 'Doctor'),
          (NURSE, 'Nurse'),
          (SURGEN, 'Surgen'),
      )
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
      # You can create Role model separately and add ManyToMany if user has more than one role
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    is_published = models.BooleanField(default=False)

    class Meta:
        permissions = [
            (
                "set_published_status",
                "Can set the status of the post to either publish or not"
            )
        ]