from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.CharField(null=False)
    address_line_1 = models.CharField(null=False)
    address_line_2 = models.CharField(null=False)
    height_in_inches = models.IntegerField(null=False)
    weight_in_lbs = models.IntegerField(null=False)
    