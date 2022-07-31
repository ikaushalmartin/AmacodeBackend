from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authentication import TokenAuthentication


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=True, null=True, default="temp")
    #email = models.EmailField(unique=True, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
  #  age = models.IntegerField(null=True, blank=True)
  #  field = models.CharField(max_length=100, null=True, blank=True)
  #  profession = models.CharField(max_length=100, null=True, blank=True)
   # university = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username


class BearerAuthentication(TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.
    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:
    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''
    keyword = 'Bearer'


