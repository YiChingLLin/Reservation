import requests
from django.conf import settings
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def inquire_view(request):
    # reservation_url = 'http://127.0.0.1:8080/api/room/inquire'
    reservation_url = settings.ROOM_BACKEND + '/api/room/inquire'
    reservation_result = requests.get(reservation_url).json()

    for i in range(len(reservation_result)):
        roomId = reservation_result[i]["RoomId"]
        # room_url = 'http://127.0.0.1:8080/api/room/roomId/'+roomId
        room_url = settings.ROOM_BACKEND + '/api/room/roomId/' + roomId
        room_result = requests.get(room_url).json()
        reservation_result[i]["RoomId"] = room_result["RoomName"]
    
    context = {
        'reservations': reservation_result,
    }

    return render(request, "inquire.html", context)

def inquire_modify_view(request):
    if request.method == "GET":
        reservationId = request.GET.get('Id')
        # reservation_url = 'http://127.0.0.1:8080/api/room/inquire/'+reservationId
        reservation_url = settings.ROOM_BACKEND + '/api/room/inquire/'+reservationId
        reservation_result = requests.get(reservation_url).json()
        rdate = reservation_result["Rdate"]
        rtime = reservation_result["Rtime"]
        rname = reservation_result["Rname"]
        rpeople = reservation_result["Rpeople"]
        rtitle = reservation_result["Rtitle"]
        rdetail = reservation_result["Rdetail"]
        roomId = reservation_result["RoomId"]
        # room_url = 'http://127.0.0.1:8080/api/room/roomId/'+roomId
        room_url = settings.ROOM_BACKEND + '/api/room/roomId/'+roomId
        room_result = requests.get(room_url).json()
        roomName = room_result["RoomName"]

        context = {
            'ReservationId' : reservationId,
            'date':rdate,
            'time':rtime,
            'name':rname,
            'people':rpeople,
            'title':rtitle,
            'detail':rdetail,
            'room':roomName
    }
        return render(request, "inquireModify.html", context)

    else:
        reservationId = request.GET.get('Id')
        # reservation_url = 'http://127.0.0.1:8080/api/room/inquire/'+reservationId
        reservation_url = settings.ROOM_BACKEND + '/api/room/inquire/'+reservationId
        reservation_result = requests.get(reservation_url).json()
        rId = reservation_result["ReservationId"]
        room = reservation_result["RoomId"]
        date = reservation_result["Rdate"]
        time = reservation_result["Rtime"]

        name = request.POST.get('inquireMname')
        people = request.POST.get('inquireMpeople')
        title = request.POST.get('inquireMtitle')
        detail = request.POST.get('inquireMdetail')

        data = {
            'ReservationId' : rId,
            'RoomId' : room,
            'Rdate' : date,
            'Rtime' : time,
            'Rname' : name,
            'Rpeople' : people,
            'Rtitle' : title,
            'Rdetail' : detail
        }

        result = requests.put(reservation_url, data)

        return HttpResponseRedirect(reverse("inquire:inquire"))

def inquire_delete_view(request):
    if request.method == "GET":
        reservationId = request.GET.get('Id')
        # reservation_url = 'http://127.0.0.1:8080/api/room/inquire/'+reservationId
        reservation_url = settings.ROOM_BACKEND + '/api/room/inquire/'+reservationId

        result = requests.delete(reservation_url)

        return HttpResponseRedirect(reverse("inquire:inquire"))

    
