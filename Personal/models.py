
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your forms here.

class Contactmessage(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    message=models.TextField()
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.first_name


class MemberImages(models.Model):
    image = models.ImageField(upload_to ='images/member')
    name = models.CharField(max_length=200 ,blank=True)
    year = models.CharField(max_length=200, blank = True)
    ability = models.CharField(max_length = 200, blank=True )
    workexperience = models.CharField(max_length = 200, blank=True )
    github = models.URLField(max_length = 200,blank=True,db_index=True, unique=True)
    community = models.URLField(max_length = 200,blank=True,db_index=True, unique=True)
    def __str__(self):
        return self.name

class Project1(models.Model):
    image = models.ImageField(upload_to ='images/project')
    topic = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    file = models.FileField(upload_to = 'documents/', blank=True)
    def __str__(self):
        return self.topic

class Student(models.Model):
    Student_ID = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(max_length=250)
    def __int__(self):
        return self.Student_ID

class Username(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField(max_length=2)
    def __str__(self):
        return self.username
