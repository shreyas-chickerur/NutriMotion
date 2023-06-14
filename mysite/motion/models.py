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

    def __str__(self):
        return self.id, self.first_name, self.last_name


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.id, self.name

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    muscle = models.CharField(max_length=30)
    equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return self.id, self.name

class WorkoutRoutine(models.Model):
    id = models.AutoField(primary_key=True)
    routine_name = models.CharField(max_length=50)
    user_id = models.ManyToManyField(User)
    exercise_ids = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.id, self.routine_name
    

class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=10000)
    category = models.CharField(max_length=10000)

    def __str__(self):
        return self.id, self.name
