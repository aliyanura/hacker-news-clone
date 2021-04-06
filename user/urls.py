from .views import RegisterAPI, LoginAPI
from django.urls import path
from knox import views

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
