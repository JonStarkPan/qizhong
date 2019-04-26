# models.py
from django.db import models
 
class Test(models.Model):
    movie_name = models.CharField(max_length=20)

class JD(models.Model):
    link = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
