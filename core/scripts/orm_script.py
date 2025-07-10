from django.db import connection
from django.utils import timezone
from core.models import Restaurant, Rating, Sale


def run():
    print("Hello world from orm_script.py!")

# Use the folloeing command to run this script:
# python manage.py  runscript orm_script 

# 1) Creating a Record in Database by (Instatiating and Saving a model object)
# We can use this same method to update as many parameters in a record.

# def run():
#     # M-1
#     restaurant=Restaurant()
#     restaurant.name="The Great Indian Restaurant"
#     restaurant.website="https://www.thegreatindianrestaurant.com"
#     restaurant.date_opened=timezone.now()
#     restaurant.latitude=28.7041
#     restaurant.longtitude=77.1025
#     restaurant.restaurant_type=Restaurant.TypeChoices.INDIAN
#     restaurant.save()  # Save the object to the database

def run():    
    # M-2
    restaurant = Restaurant.objects.create(
        name="The Great Chinese Restaurant",
        website="https://www.thegreatchineserestaurant.com",
        date_opened=timezone.now(),
        latitude=28.7041,
        longtitude=77.1025,
        restaurant_type=Restaurant.TypeChoices.CHINESE
    )
    print(restaurant)  # Print the created restaurant object
    print(connection.queries)  # Print the SQL queries executed for the above operation

# Querying the Database with ORM
def run():
    
    # # Fetching all restaurants
    # restaurants = Restaurant.objects.all()
    # print(restaurants)

    # # Fetching the first restaurant
    # first_restaurant = Restaurant.objects.first()

    # # Indexing into django querysets
    # first_restaurant=Restaurant.objects.all()[0]
    # print(first_restaurant)

    # # Fetching the last restaurant
    # last_restaurant=Restaurant.objects.last()
    # print(last_restaurant)
    # print(connection.queries)  # Print the SQL queries executed for the above operation

    # Counting number of restaurants 
    restaurant_count = Restaurant.objects.count()
    print(restaurant_count)
    print(connection.queries)  # Print the SQL queries executed for the above operation
    
    

    