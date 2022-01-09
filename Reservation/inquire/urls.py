from django.urls import path, re_path
from . import views

app_name = "inquire"
urlpatterns = [
    path("", views.inquire_view, name="inquire"),
    re_path(r'^modify/$', views.inquire_modify_view, name="inquire_modify"),
    re_path(r'^delete/$', views.inquire_delete_view, name="inquire_delete")
]