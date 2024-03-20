from django.urls import path, re_path, include
from django.contrib import admin
from users import views
from users.views import insert

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("", views.index, name="index"),
    path("insert/", insert),
    path("users/recommend1/", views.recommend1),
    path("users/recommend2/", views.recommend2),
    re_path(r"^users/recommend1/users/recommend1/recommend2/$", views.recommend2),
    # path('users/showmessage/', views.showmessage),
]
