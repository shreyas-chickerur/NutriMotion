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


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=30)
    date_gathered = models.DateField()
    source_link = models.CharField()
    # macros_list = 
    recipe_count = models.IntegerField(default=-1)

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=30)
    source_link = models.CharField()
    ingredients = models.ManyToManyField(Ingredient)

class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=30)
    source_link = models.CharField()
    recipes = models.ManyToManyField(Recipe)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Mealplan(models.Model):
    id = models.AutoField(primary_key=True)
    source_link = models.CharField()
    meals = models.ManyToManyField(Meal)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

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
    link = models.CharField()
    category = models.CharField()
