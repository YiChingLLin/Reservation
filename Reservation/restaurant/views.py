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

def restaurant_view(request):
    # restaurant_url = 'http://127.0.0.1:8081/api/restaurant/restaurant'
    restaurant_url = settings.RESTAURANT_BACKEND + '/api/restaurant/restaurant'
    restaurant_result = requests.get(restaurant_url)

    # chain_url = 'http://127.0.0.1:8081/api/restaurant/chain'
    chain_url = settings.RESTAURANT_BACKEND + '/api/restaurant/chain'
    chain_result = requests.get(chain_url)

    # time_url = 'http://127.0.0.1:8081/api/restaurant/time'
    time_url = settings.RESTAURANT_BACKEND + '/api/restaurant/time'
    time_result = requests.get(time_url)

    if request.GET.get('restaurantdate')!='':
        date = request.GET.get('restaurantdate')

    context = {
        'restaurants': restaurant_result.json(),
        'chains': chain_result.json(),
        'times': time_result.json(),
        'date' : date
    }

    return render(request, "restaurant.html", context)
    
def restaurant_reservation_view(request):
    if request.method == "GET":
        chain = request.GET.get('chain')

        # chain_url = 'http://127.0.0.1:8081/api/restaurant/chainName/'+chain
        chain_url = settings.RESTAURANT_BACKEND + '/api/restaurant/chainName/'+chain
        chain_result = requests.get(chain_url).json()
        chainopentime = chain_result["ChainOpenTime"]
        time = request.GET.get('time')
        date = request.GET.get('date')

        context = {
            'chain':chain,
            'opentime':chainopentime,
            'date':date,
            'time':time
        }
        return render(request, "restaurantReservation.html", context)

    else:
        # reservation_url = 'http://127.0.0.1:8081/api/restaurant/inquire'
        reservation_url = settings.RESTAURANT_BACKEND + '/api/restaurant/inquire'

        time = request.GET.get('time')
        chain = request.GET.get('chain')
        # chain_url = 'http://127.0.0.1:8081/api/restaurant/chainName/'+chain
        chain_url = settings.RESTAURANT_BACKEND + '/api/restaurant/chainName/'+chain
        chain_result = requests.get(chain_url).json()
        chainId = chain_result["ChainId"]

        date = request.GET.get('date')
        name = request.POST.get('restaurantRname')
        people = request.POST.get('restaurantRpeople')
        detail = request.POST.get('restaurantRdetail')

        data = {
            'ChainId' : chainId,
            'Rdate' : date,
            'Rtime' : time,
            'Rname' : name,
            'Rpeople' : people,
            'Rdetail' : detail
        }

        result = requests.post(reservation_url, data)

        return HttpResponseRedirect(reverse("restaurant:restaurant"))