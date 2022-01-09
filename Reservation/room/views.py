from django.http.response import JsonResponse
import requests
from django.conf import settings
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.urls import reverse

# Create your views here.

def room_view(request):
    # company_url = 'http://127.0.0.1:8080/api/room/company'
    company_url = settings.ROOM_BACKEND + '/api/room/company'
    company_result = requests.get(company_url)

    # room_url = 'http://127.0.0.1:8080/api/room/room'
    room_url = settings.ROOM_BACKEND + '/api/room/room'
    room_result = requests.get(room_url)

    # time_url = 'http://127.0.0.1:8080/api/room/time'
    time_url = settings.ROOM_BACKEND + '/api/room/time'
    time_result = requests.get(time_url)

    if request.GET.get('roomdate')!='':
        date = request.GET.get('roomdate')

    context = {
        'companies': company_result.json(),
        'rooms': room_result.json(),
        'times': time_result.json(),
        'date' : date
    }

    return render(request, "room.html", context)
    
def room_reservation_view(request):
    if request.method == "GET":
        room = request.GET.get('room')
        time = request.GET.get('time')
        date = request.GET.get('date')
        context = {
            'room':room,
            'date':date,
            'time':time
        }
        return render(request, "roomReservation.html", context)

    else:
        # reservation_url = 'http://127.0.0.1:8080/api/room/inquire'
        reservation_url = settings.ROOM_BACKEND + '/api/room/inquire'

        time = request.GET.get('time')
        room = request.GET.get('room')
        # room_url = 'http://127.0.0.1:8080/api/room/roomName/'+room
        room_url = settings.ROOM_BACKEND + '/api/room/roomName/'+room
        room_result = requests.get(room_url).json()
        roomId = room_result["RoomId"]

        date = request.GET.get('date')
        name = request.POST.get('roomRname')
        people = request.POST.get('roomRpeople')
        title = request.POST.get('roomRtitle')
        detail = request.POST.get('roomRdetail')

        data = {
            'RoomId' : roomId,
            'Rdate' : date,
            'Rtime' : time,
            'Rname' : name,
            'Rpeople' : people,
            'Rtitle' : title,
            'Rdetail' : detail
        }

        result = requests.post(reservation_url, data)

        return HttpResponseRedirect(reverse("room:room"))