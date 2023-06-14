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

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=30)
    date_gathered = models.DateField()
    source_link = models.CharField(max_length=10000)
    macros_list = models.CharField(max_length=10000)
    recipe_count = models.IntegerField(default=-1)

    def __str__(self):
        return self.id, self.ingredient_name

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=30)
    source_link = models.CharField(max_length=10000)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.id, self.recipe_name

class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=30)
    source_link = models.CharField(max_length=10000)
    recipes = models.ManyToManyField(Recipe)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id, self.meal_name

class Mealplan(models.Model):
    id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=30)
    source_link = models.CharField(max_length=10000)
    meals = models.ManyToManyField(Meal)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id, self.plan_name