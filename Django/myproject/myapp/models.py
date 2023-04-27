from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    usda_id = models.CharField(max_length=10, unique=True)
