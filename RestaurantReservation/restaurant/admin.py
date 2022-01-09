from django.contrib import admin
from .models import Restaurant, Chain, AvailableTime, RestaurantReservation

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Chain)
admin.site.register(AvailableTime)
admin.site.register(RestaurantReservation)