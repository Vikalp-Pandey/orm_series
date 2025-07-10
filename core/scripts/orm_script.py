from django.utils import timezone
from core.models import Restaurant, Rating, Sale


def run():
    print("Hello world from orm_script.py!")

# Use the folloeing command to run this script:
# python manage.py  runscript orm_script 

# Creating a Record in Database by (Instatiating and Saving a model object)
# We can use this same method to update as many parameters in a record.
def run():
    # M-1
    restaurant=Restaurant()
    restaurant.name="The Great Indian Restaurant"
    restaurant.website="https://www.thegreatindianrestaurant.com"
    restaurant.date_opened=timezone.now()
    restaurant.latitude=28.7041
    restaurant.longtitude=77.1025
    restaurant.restaurant_type=Restaurant.TypeChoices.INDIAN
    restaurant.save()  # Save the object to the database


    