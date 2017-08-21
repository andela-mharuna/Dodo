from django.db import models

# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length=60)
  email = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  image = models.CharField(max_length=200)
