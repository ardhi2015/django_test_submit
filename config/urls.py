from django.conf.urls import include
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("", include("core.service.urls")),
    path("earthquake", include("core.earthquake.urls")),
    path("wall/", include("core.wall.urls")),
    path("weather", include("core.weather.urls")),
    # Documentation
    path(
        "docs/schema",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "docs/redoc",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
