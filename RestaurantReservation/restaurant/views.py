from django.shortcuts import render
from rest_framework import viewsets, status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant, Chain, AvailableTime, RestaurantReservation
from .serializers import RestaurantSerializer, ChainSerializer, TimeSerializer, ReservationSerializer
# Create your views here.

class RestaurantViewSet(viewsets.ViewSet):
    def list(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = RestaurantSerializer (data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ChainViewSet(viewsets.ViewSet):
    def list(self, request):
        chains = Chain.objects.all()
        serializer = ChainSerializer(chains, many=True)
        return Response(serializer.data)
    
    def listchainId(self, request, pkname=None):
        chain = Chain.objects.get(ChainName=pkname)
        serializer = ChainSerializer(chain)
        return Response(serializer.data)

    def listchainName(self, request, pk=None):
        chain = Chain.objects.get(ChainId=pk)
        serializer = ChainSerializer(chain)
        return Response(serializer.data)

class TimeViewSet(viewsets.ViewSet):
    def list(self, request):
        times = AvailableTime.objects.all()
        serializer = TimeSerializer(times, many=True)
        return Response(serializer.data)

class ReservationViewSet(viewsets.ViewSet):
    def list(self, request):
        reservations = RestaurantReservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    def listR(self, request, pk=None):
        reservation = RestaurantReservation.objects.get(ReservationId=pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReservationSerializer (data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        reservation = RestaurantReservation.objects.get(ReservationId=pk)
        serializer = ReservationSerializer(instance=reservation, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        reservation = RestaurantReservation.objects.get(ReservationId=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
