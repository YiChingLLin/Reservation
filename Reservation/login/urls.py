from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_user, name="logout_user"),
    path("login/", views.select_view, name="afterLogin"),
]