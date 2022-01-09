from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login:login"))

def login_view(request):
    if request.method == "GET":
        context = {
            'user': "",
            'error_text': ""
        }
        return render(request, "login.html", context)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponseRedirect(reverse("login:afterLogin"))
        else:
            context = {
                'user': username,
                'error_text': "Login Fail!"
            }
            return render(request, "login.html", context)

def select_view(request):
    return render(request, "afterLogin.html")