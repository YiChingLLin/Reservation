from django.urls import path, re_path
from . import views

app_name = "room"
urlpatterns = [
    path("", views.room_view, name="room"),
    re_path(r'^reservation/$', views.room_reservation_view, name="room_reservation")
]