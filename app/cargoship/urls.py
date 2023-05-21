from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup, name="signup"),
    path("containers/", views.containers, name="containers"),
]
