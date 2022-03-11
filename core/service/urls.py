from django.urls import path

from .views import LoginView, RegisterView, hello_world

urlpatterns = [
    path("", hello_world, name="index"),
    path("login", LoginView.as_view()),
    path("register", RegisterView.as_view()),
]
