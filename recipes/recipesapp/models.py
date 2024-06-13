from django.db import models


# Create your models here.
class Recipe(models.Model):
    CATEGORY_CHOICES=[
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
        ('Dessert', 'Dessert'),
    ]
    title=models.CharField(max_length=100)
    ingredients=models.TextField()
    instructions=models.TextField()
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

