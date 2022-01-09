from rest_framework import serializers
from .models import Restaurant, Chain, AvailableTime, RestaurantReservation


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('RestaurantName',)

class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = ('ChainName','ChainId', 'ChainOpenTime')

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = ('Time1','Time2','Time3','Time4','Time5')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReservation
        fields = ('Rdate','Rtime','Rname','Rpeople','Rdetail','ChainId','ReservationId')