from django.shortcuts import render
from rest_framework import viewsets, status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AvailableTime, Company, Room, AvailableTime, RoomReservation
from .serializers import CompanySerializer, RoomSerializer, TimeSerializer, ReservationSerializer
# Create your views here.

class CompanyViewSet(viewsets.ViewSet):
    def list(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CompanySerializer (data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RoomViewSet(viewsets.ViewSet):
    def list(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
    def listroomId(self, request, pkname=None):
        room = Room.objects.get(RoomName=pkname)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def listroomName(self, request, pk=None):
        room = Room.objects.get(RoomId=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

class TimeViewSet(viewsets.ViewSet):
    def list(self, request):
        times = AvailableTime.objects.all()
        serializer = TimeSerializer(times, many=True)
        return Response(serializer.data)

class ReservationViewSet(viewsets.ViewSet):
    def list(self, request):
        reservations = RoomReservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    def listR(self, request, pk=None):
        reservation = RoomReservation.objects.get(ReservationId=pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReservationSerializer (data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        reservation = RoomReservation.objects.get(ReservationId=pk)
        serializer = ReservationSerializer(instance=reservation, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        reservation = RoomReservation.objects.get(ReservationId=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
