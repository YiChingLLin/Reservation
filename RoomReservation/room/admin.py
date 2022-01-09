from django.contrib import admin
from .models import Company,Room,AvailableTime,RoomReservation

# Register your models here.
admin.site.register(Company)
admin.site.register(Room)
admin.site.register(AvailableTime)
admin.site.register(RoomReservation)