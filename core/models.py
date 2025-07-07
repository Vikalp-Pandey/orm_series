from django.db import models

# Create your models here.
'''Restaurant Management System'''

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    website=models.URLField(default='')
    date_opened=models.DateField()
    latitude=models.FloatField()
    longtitude=models.FloatField()

    def __str__(self):
        return self.name