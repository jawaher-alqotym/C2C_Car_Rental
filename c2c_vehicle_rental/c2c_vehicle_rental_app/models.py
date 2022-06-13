from django.db import models
from users_app import models as users_app_models

VEHICLE_CATEGORY_CHOICES = [
        ('Jeep', 'jeep'),
        ('Minivan', 'minivan'),
        ('Truck', 'Truck'),
        ('Car', 'car'),
    ]

HOURLY_RENTAL_PRICE_CHOICES = [
        ('economical', 20),
        ('mid', 30),
        ('luxury', 40),
]



class Vehicle(models.Model):
    '''
    this model contains the Vehicle info
    '''
    owner = models.ForeignKey(users_app_models.UserCredential, related_name= 'Vehicle',on_delete=models.CASCADE)
    vehicle_brand = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="images/Vehicles_pic")
    category = models.CharField(max_length=25, choices=VEHICLE_CATEGORY_CHOICES,default='Car')
    rating_avg = models.DecimalField(max_digits=3, decimal_places=2, help_text='The vehicle owner/rentee ratings average')
    year_of_making = models.DateTimeField(default='2013-01-01 00:00:00')
    hourly_rental_price = models.IntegerField(choices=HOURLY_RENTAL_PRICE_CHOICES,default='economical')
    location = models.CharField(max_length=250, help_text='The location of the vehicle')




class Reviwes(models.Model):
    '''
    this model contains the reviews about each user being a vehicle owner or vehicle rentee
    '''
    author = models.ForeignKey(users_app_models.UserCredential, related_name= 'Reviwes',on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=140)


class Booking(models.Model):
    '''
    this model contains the booking info
    '''
    vehicle = models.ForeignKey(Vehicle, related_name= 'Vehicle_Booking',on_delete=models.CASCADE)
    rentee = models.ForeignKey(users_app_models.UserCredential, related_name= 'rentee_Booking',on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True, help_text='Vehicle received date')
    end_date = models.DateTimeField(null=False, help_text= 'Vehicle return date, at least 5 hours after vehicle received date')
    vehicle_delivery = models.BooleanField(default=False, help_text='Does the rentee wants the vehicle delevered to them or not')
    cost = models.DecimalField(max_digits=5, decimal_places=2, help_text='The total cost of renting the vehicle for N hours + 20% of renting cost if the user wants the vehicle deliverd to them')
