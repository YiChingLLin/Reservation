import requests
from django.conf import settings
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def rinquire_view(request):
    # reservation_url = 'http://127.0.0.1:8081/api/restaurant/inquire'
    reservation_url = settings.RESTAURANT_BACKEND + '/api/restaurant/inquire'
    reservation_result = requests.get(reservation_url).json()

    for i in range(len(reservation_result)):
        chainId = reservation_result[i]["ChainId"]
        # chain_url = 'http://127.0.0.1:8081/api/restaurant/chainId/'+ chainId
        chain_url = settings.RESTAURANT_BACKEND + '/api/restaurant/chainId/'+ chainId
        chain_result = requests.get(chain_url).json()
        reservation_result[i]["ChainId"] = chain_result["ChainName"]
    
    context = {
        'reservations': reservation_result,
    }

    return render(request, "restaurantInquire.html", context)

def rinquire_modify_view(request):
    if request.method == "GET":
        reservationId = request.GET.get('Id')
        # reservation_url = 'http://127.0.0.1:8081/api/restaurant/inquire/'+reservationId
        reservation_url = settings.RESTAURANT_BACKEND + '/api/restaurant/inquire/'+reservationId
        reservation_result = requests.get(reservation_url).json()
        rdate = reservation_result["Rdate"]
        rtime = reservation_result["Rtime"]
        rname = reservation_result["Rname"]
        rpeople = reservation_result["Rpeople"]
        rdetail = reservation_result["Rdetail"]
        chainId = reservation_result["ChainId"]
        # chain_url = 'http://127.0.0.1:8081/api/restaurant/chainId/'+chainId
        chain_url = settings.RESTAURANT_BACKEND + '/api/restaurant/chainId/'+chainId
        chain_result = requests.get(chain_url).json()
        chainName = chain_result["ChainName"]

        context = {
            'ReservationId' : reservationId,
            'date':rdate,
            'time':rtime,
            'name':rname,
            'people':rpeople,
            'detail':rdetail,
            'chain':chainName
    }
        return render(request, "restaurantInquireModify.html", context)

    else:
        reservationId = request.GET.get('Id')
        # reservation_url = 'http://127.0.0.1:8081/api/restaurant/inquire/'+reservationId
        reservation_url = settings.RESTAURANT_BACKEND + '/api/restaurant/inquire/'+reservationId
        reservation_result = requests.get(reservation_url).json()
        rId = reservation_result["ReservationId"]
        chain = reservation_result["ChainId"]
        date = reservation_result["Rdate"]
        time = reservation_result["Rtime"]

        name = request.POST.get('inquireMname')
        people = request.POST.get('inquireMpeople')
        detail = request.POST.get('inquireMdetail')

        data = {
            'ReservationId' : rId,
            'RoomId' : chain,
            'Rdate' : date,
            'Rtime' : time,
            'Rname' : name,
            'Rpeople' : people,
            'Rdetail' : detail
        }

        result = requests.put(reservation_url, data)

        return HttpResponseRedirect(reverse("restaurantInquire:rinquire"))

def rinquire_delete_view(request):
    if request.method == "GET":
        reservationId = request.GET.get('Id')
        # reservation_url = 'http://127.0.0.1:8081/api/restaurant/inquire/'+reservationId
        reservation_url = settings.RESTAURANT_BACKEND + '/api/restaurant/inquire/'+reservationId

        result = requests.delete(reservation_url)

        return HttpResponseRedirect(reverse("restaurantInquire:rinquire"))

    
