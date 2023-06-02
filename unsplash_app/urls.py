from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("login", views.login, name="login")
]
