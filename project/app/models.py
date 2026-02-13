from django.db import models

# Create your models here.

class emp(models.Model):
    n=models.CharField(max_length=50)
    a=models.IntegerField(max_length=10)
    c=models.IntegerField(max_length=15)
    e=models.EmailField(max_length=30)
    d=models.CharField(max_length=50)
    
class dep(models.Model):
    d=models.CharField()
    h=models.CharField(max_length=50)