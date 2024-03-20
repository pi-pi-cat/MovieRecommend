from django.urls import path, re_path
from . import views

app_name = "users"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("showmessage/", views.showmessage, name="showmessage"),
]
