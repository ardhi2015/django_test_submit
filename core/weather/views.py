from core.utils.responses import Responses
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weather
from .serializers import (
    WeatherGetResponseSerializer,
    WeatherPostResponseSerializer,
    WeatherSerializer,
)


class WeatherView(APIView):
    @extend_schema(
        request=None,
        responses={200: WeatherGetResponseSerializer},
    )
    def get(self, request):
        """
        Return a list of all weather data.
        """

        weathers = Weather.objects.all()
        serializer = WeatherSerializer(weathers, many=True)
        return Response(Responses.success(serializer.data))

    @extend_schema(
        request=WeatherSerializer,
        responses={200: WeatherPostResponseSerializer},
        examples=[
            OpenApiExample(
                "Example 1",
                request_only=True,
                value={
                    "date": "2020-01-01",
                    "weathercode": 0,
                    "temperature": 25.0,
                    "max_temperature": 32.0,
                    "min_temperature": 21.0,
                    "sunrise": "2020-01-01T23:00:00Z",
                    "sunset": "2020-01-01T11:00:00Z",
                },
            ),
        ],
    )
    def post(self, request):
        """
        Create a new weather data.
        """

        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Responses.success(serializer.data))
        else:
            return Response(Responses.error(str(serializer.errors)), status=400)
