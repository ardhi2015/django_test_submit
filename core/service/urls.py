from django.urls import path

from .views import LoginView, RegisterView, hello_world

urlpatterns = [
    path("", hello_world, name="index"),
    path("login", LoginView.as_view(), name ='login'),
    path("register", RegisterView.as_view(), name ='register'),
]
