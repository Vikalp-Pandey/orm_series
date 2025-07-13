from django.db import connection
from django.utils import timezone
from core.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User

def run():
    print("Hello world from orm_script.py!")

# Use the folloeing command to run this script:
# python manage.py  runscript orm_script 

# 1) Creating a Record in Database by (Instatiating and Saving a model object)
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

def run():    
    # M-2
    restaurant = Restaurant.objects.create(
        name="The Italian Bistro",
        website="https://www.theitalianbistro.com",
        date_opened=timezone.now(),
        latitude=28.5041,
        longtitude=77.1025,
        restaurant_type=Restaurant.TypeChoices.ITALIAN
    )
    print(restaurant)  # Print the created restaurant object
    print(restaurant.name)  # Print the created restaurant object's name


# 2) Updating a Record in Database by (Instatiating and Saving a model object)

    restaurant.latitude = 28.7041  # Update the latitude
    restaurant.save()  # Save the updated object to the database
    print(restaurant.latitude)  # Print the updated latitude
    print(connection.queries)  # Print the SQL queries executed for the above operation



#3)  Querying the Database with ORM
def run():
    
    # Fetching all restaurants
    restaurants = Restaurant.objects.all()
    print(restaurants)

    # Fetching the first restaurant
    first_restaurant = Restaurant.objects.first()

    # Indexing into django querysets
    first_restaurant=Restaurant.objects.all()[0]
    print(first_restaurant)

    # Fetching the last restaurant
    last_restaurant=Restaurant.objects.last()
    print(last_restaurant)
    print(connection.queries)  # Print the SQL queries executed for the above operation

    # Counting number of restaurants 
    restaurant_count = Restaurant.objects.count()
    print(restaurant_count)
    print(connection.queries)  # Print the SQL queries executed for the above operation
    
    
def run():
    restaurant=Restaurant.objects.first() # Fetching the first restaurant
    user=User.objects.first()            # Fetching the first user instance
    
    Rating.objects.create(restaurant=restaurant, user=user, rating=4.5)
    # passing the restaurant and user objects directly to the create method


# 4) Filtering and Excluding Records in Database using ORM
def run():
    # Filtering the restaurants based on a condition.
    filtered_rating=Rating.objects.filter(rating=4)
    print(filtered_rating)
    print(connection.queries)  # Print the SQL queries executed for the above operation

    # Filtering based on a lookup
    filtered_rating = Rating.objects.filter(rating__gte=3)  # Greater than or equal to 4.5
    filtered_rating = Rating.objects.filter(rating__lte=3)  # Lesser than or equal to 4.5
    print(filtered_rating)

    # Excluding records based on a condition
    excluded_rating = Rating.objects.exclude(rating=4)  # Exclude ratings

    # Lookups
    excluded_rating = Rating.objects.exclude(rating__lte=4)  # Exclude ratings
    print(excluded_rating)
    

# 5) Querying related objects in ORM
def run():
    rating=Rating.objects.first()  # Fetching the first rating
    restaurant=rating.restaurant  # Accessing the related Foriegn Key restaurant object on whom the rating was given
    print(restaurant)  # Print the restaurant object
    print(restaurant.name)  # Print the name of the restaurant

# 6) Querying related objects in ORM using reverse relation
def run():
    restaurant = Restaurant.objects.first()  # Fetching the first restaurant
    
    # M-1
    # ratings = restaurant.rating_set.all()  # Accessing all ratings related to the restaurant
    # print(ratings)  # Print all ratings for the restaurant

    # M-2
    ratings=restaurant.ratings.all()  # Accessing all ratings related to the restaurant using the related name
    print(ratings)  # Print all ratings for the restaurant
 

def run():
    Sale.objects.create(
        restaurant=Restaurant.objects.first(),  # Fetching the first restaurant
        income=1000.00,
        datetime=timezone.now()
    )
    Sale.objects.create(
        restaurant=Restaurant.objects.first(),  # Fetching the first restaurant
        income=2000.00,
        datetime=timezone.now()
    )
    Sale.objects.create(
        restaurant=Restaurant.objects.first(),  # Fetching the first restaurant
        income=3000.00,
        datetime=timezone.now()
    )
    



def run():
    restaurant = Restaurant.objects.first()  # Fetching the first restaurant
    sales = restaurant.sales.all()  # Accessing all sales related to the restaurant using the related name
    print(sales)  # Print all sales for the restaurant

    # Accessing the first sale of the restaurant
    first_sale = sales.first()
    print(first_sale)  # Print the first sale object

# Fetching or Creating data with Model.objects.get_or_create()
def run():
    user=User.objects.first()
    restaurant=Restaurant.objects.last()
    # Fetching or creating(boolean)  a rating for the restaurant by the user
    rating,created=Rating.objects.get_or_create(
        restaurant=restaurant,
        user=user,
        rating=3
    )
    print(rating,created) # Print the rating object and whether it was created or fetched

    if created:
        # Provide Some Conditional Logic
        print("Rating was created")
    if rating:
        # Provide Other Conditional Logic
        print("Rating already exists")
    print(connection.queries)
    
def run():
    user=User.objects.first()  # Fetching the first user
    restaurant=Restaurant.objects.first()  # Fetching the first restaurant
    
    rating=Rating.objects.create(
        user=user,
        restaurant=restaurant,
        rating=9
    )    

    rating.full_clean()  # This will raise a ValidationError if the rating is not valid
    