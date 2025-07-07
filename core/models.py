from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''Restaurant Management System'''

# 1) Restaurant Model
class Restaurant(models.Model):   
    '''Restaurant Class is Inhereting form django.db.models.Model'''
    class TypeChoices(models.TextChoices):
        INDIAN="IN" "Indian"
        CHINESE="CH" "Chinese"
        ITALIAN="IT" "Italian"
        GREEK="GR" "Greek"
        MEXICAN="Mx" "Mexican"
        FASTFOOD="FF" "Fastfood"
        OTHERS="OT" "Others"


    name=models.CharField(max_length=100)
    website=models.URLField(default='')
    date_opened=models.DateField()
    latitude=models.FloatField()
    longtitude=models.FloatField()
    Restaurant_type=models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name
        # Human-readable representation of a Restaurant object


# 2) Built-in User Model

# 3) Rating  Model: Rating should be done by a User defined in users Table and on Rstaurant defined in Restaurant Table.
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    rating=models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating : {self.rating}"
    # Human-readable representation of a Rating object


