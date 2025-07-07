from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''Restaurant Management System'''

# 1) Restaurant Model
class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    website=models.URLField(default='')
    date_opened=models.DateField()
    latitude=models.FloatField()
    longtitude=models.FloatField()

    def __str__(self):
        return self.name
    
# 2) Built-in User Model

# 3) Rating  Model
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    rating=models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating : {self.rating}"


