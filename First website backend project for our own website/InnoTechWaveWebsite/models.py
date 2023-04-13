from django.db import models
from accounts.models import User

class Projects(models.Model):
    name=models.CharField(max_length=1000,blank=False)
    description=models.TextField(max_length=10000,blank=False)
    url = models.URLField(max_length=1000, blank=True)
    cover=models.ImageField(upload_to='images/',blank=False)
    addBy=models.ForeignKey(User, on_delete=models.SET_NULL,related_name='projects',null=True,blank=True)
    

    def __str__(self):
        return self.id

class DomainWork(models.Model):
    name=models.CharField(max_length=1000,blank=False)
    description=models.TextField(max_length=10000,blank=False)
    photo=models.ImageField(upload_to='images/',blank=False)
    createBy=models.ForeignKey(User, on_delete=models.SET_NULL,related_name='domains',null=True,blank=True)


    def __str__(self):
        return self.id


class OurServices(models.Model):
    name=models.CharField(max_length=1000,blank=False)
    description=models.TextField(max_length=10000,blank=False)
    addBy=models.ForeignKey(User, on_delete=models.SET_NULL,related_name='services',null=True,blank=True)


    def __str__(self):
        return self.id


class SubscribeWebsite(models.Model):

    email=models.EmailField(max_length=255,unique=True)

    def __str__(self):
        return self.id