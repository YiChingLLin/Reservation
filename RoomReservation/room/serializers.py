from rest_framework import serializers
from .models import AvailableTime, Company, Room, AvailableTime, RoomReservation


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('CompanyName', 'CompanyOpenTime', 'CompanyAddress')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('RoomName','RoomId')

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = ('Time1','Time2','Time3','Time4','Time5')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = ('Rdate','Rtime','Rname','Rpeople','Rtitle','Rdetail','RoomId','ReservationId')