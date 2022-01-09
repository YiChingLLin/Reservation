from django.urls import path, re_path
from . import views

app_name = "restaurant"
urlpatterns = [
    path("", views.restaurant_view, name="restaurant"),
    re_path(r'^reservation/$', views.restaurant_reservation_view, name="restaurant_reservation")
]