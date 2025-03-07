from django.contrib import admin
from django.urls import include, path

from users.views import login_page, register_page, users_page


app_name = "users"

urlpatterns = [
    path("", users_page),
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
]
