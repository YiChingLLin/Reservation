from django.db import models
from django.utils import timezone

# Create your models here.
class Restaurant (models.Model):
    RestaurantId = models.CharField(max_length=100, unique=True, primary_key=True)
    RestaurantName = models.CharField(max_length=200)
    def __str__(self):
        return self.RestaurantName

class Chain (models.Model):
    ChainId = models.CharField(max_length=100, unique=True , primary_key=True)
    ChainName = models.CharField(max_length=200)
    ChainOpenTime = models.CharField(max_length=100)
    RestaurantName = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.ChainName

class AvailableTime (models.Model):
    RestaurantName = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE, default=0)
    Time1 = models.CharField(max_length=200)
    Time2 = models.CharField(max_length=200)
    Time3 = models.CharField(max_length=200)
    Time4 = models.CharField(max_length=200)
    Time5 = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.RestaurantName

class RestaurantReservation (models.Model):
    ReservationId = models.AutoField(auto_created=True, primary_key=True, unique=True)
    UserId = models.IntegerField
    DateTime = models.DateTimeField(default=timezone.now)
    Rdate = models.CharField(max_length=200)
    Rtime = models.CharField(max_length=200)
    Rname = models.CharField(max_length=100)
    Rpeople = models.CharField(max_length=100)
    Rdetail = models.CharField(max_length=200, default="無")
    ChainId = models.ForeignKey('restaurant.Chain', on_delete = models.DO_NOTHING, default=0)
