from django.urls import path

from .views import EarthquakeView

urlpatterns = [
    path("", EarthquakeView.as_view(), name="index"),
]
