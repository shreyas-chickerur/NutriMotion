from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    height_in_inches = models.IntegerField(default=-1)
    weight_in_lbs = models.IntegerField(default=-1)


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    muscle = models.CharField(max_length=30)
    equipment = models.ManyToManyField(Equipment)

class WorkoutRoutine(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ManyToManyField(User)
    exercise_ids = models.ManyToManyField(Exercise)
    

class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=10000)
    category = models.CharField(max_length=10000)
