from django.db import models
from django.utils import timezone

# Create your models here.
class Company (models.Model):
    CompanyId = models.CharField(max_length=100, unique=True, primary_key=True)
    CompanyName = models.CharField(max_length=200)
    CompanyOpenTime = models.CharField(max_length=100)
    CompanyAddress= models.CharField(max_length=300)
    def __str__(self):
        return self.CompanyName

class Room (models.Model):
    RoomId = models.CharField(max_length=100, unique=True , primary_key=True)
    RoomName = models.CharField(max_length=200)
    CompanyName = models.ForeignKey('room.Company', on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.RoomName

class AvailableTime (models.Model):
    CompanyName = models.ForeignKey('room.Company', on_delete=models.CASCADE, default=0)
    Time1 = models.CharField(max_length=200)
    Time2 = models.CharField(max_length=200)
    Time3 = models.CharField(max_length=200)
    Time4 = models.CharField(max_length=200)
    Time5 = models.CharField(max_length=200)
    def __str__(self):
        return self.CompanyName

class RoomReservation (models.Model):
    ReservationId = models.AutoField(auto_created=True, primary_key=True, unique=True)
    UserId = models.IntegerField
    DateTime = models.DateTimeField(default=timezone.now)
    Rdate = models.CharField(max_length=200)
    Rtime = models.CharField(max_length=200)
    Rname = models.CharField(max_length=100)
    Rpeople = models.CharField(max_length=100)
    Rtitle = models.CharField(max_length=200)
    Rdetail = models.CharField(max_length=200, default="無")
    RoomId = models.ForeignKey('room.Room', on_delete = models.DO_NOTHING, default=0)
