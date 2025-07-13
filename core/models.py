from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
'''Restaurant Management System'''

# 1) Restaurant Model
class Restaurant(models.Model):   
    '''Restaurant Class is Inhereting form django.db.models.Model'''
    class TypeChoices(models.TextChoices):
        INDIAN="IN","Indian"
        CHINESE="CH","Chinese"
        ITALIAN="IT","Italian"
        GREEK="GR","Greek"
        MEXICAN="MX","Mexican"
        FASTFOOD="FF","Fastfood"
        OTHERS="OT","Others"


    name=models.CharField(max_length=100)
    website=models.URLField(default='')
    date_opened=models.DateField()
    latitude=models.FloatField()
    longtitude=models.FloatField()
    restaurant_type=models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name
        # Human-readable representation of a Restaurant object


# 2) Built-in User Model

# 3) Rating  Model: Rating should be done by a User defined in users Table and on Rstaurant defined in Restaurant Table.
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='ratings') 
    # related_name allows reverse access to ratings from Restaurant
    # We can use ratings as a placeholder to access all ratings of a restaurant instead of using the default 'rating_set' method.
    rating=models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),  # Minimum value for rating
            MaxValueValidator(5)   # Maximum value for rating
        ],
        
    )
    # Rating should be between 0 and 5.So we use PositiveSmallIntegerField with validators.

    def __str__(self):
        return f"Rating : {self.rating}"
    # Human-readable representation of a Rating object


# 4) Sale Model
class Sale(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True,related_name='sales')
    income=models.DecimalField(max_digits=8,decimal_places=2)
    datetime=models.DateTimeField()
    