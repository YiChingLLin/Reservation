from django.urls import path, re_path
from . import views

app_name = "restaurantInquire"
urlpatterns = [
    path("", views.rinquire_view, name="rinquire"),
    re_path(r'^modify/$', views.rinquire_modify_view, name="rinquire_modify"),
    re_path(r'^delete/$', views.rinquire_delete_view, name="rinquire_delete")
]