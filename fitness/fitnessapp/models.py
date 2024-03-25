from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70) 

    def  __str__(self):
        return self.username
    
class Activity(models.Model):
    name = models.CharField(max_length=100)

    def  __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newactivity = models.CharField(max_length=70,default="")
    

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    target = models.FloatField()

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)