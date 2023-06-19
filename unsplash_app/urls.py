from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="sign-up"),
    path("<str:user_name>", views.logged_in, name="logged-in-succ")
]
