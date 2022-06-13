
from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ['owner','vehicle_brand',
                  'pic', 'category',
                  'year_of_making',
                  'hourly_rental_price',
                  'location']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['vehicle', 'rentee', 'start_date' , 'end_date', 'vehicle_delivery']


class ReviwesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviwes
        fields = "__all__"