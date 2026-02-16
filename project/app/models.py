from django.db import models

# Create your models here.

class emp(models.Model):
    n=models.CharField(max_length=50)
    a=models.IntegerField(null=True)
    c=models.IntegerField(null=True)
    e=models.EmailField(null=True)
    d=models.CharField(max_length=50)
    
class dep(models.Model):
    d=models.CharField()
    h=models.CharField(max_length=50)
    
    
class submit_que(models.Model):
    n=models.CharField(max_length=50)
    e=models.EmailField(null=True)
    c=models.CharField(max_length=50)
    d=models.CharField(max_length=50)
    q=models.CharField(max_length=100)
    