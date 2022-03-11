from core.utils.earthquake import Earthquakes
from core.utils.responses import Responses
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EarthquakeGetResponseSerializer, EarthquakeSerializer


class EarthquakeView(APIView):
    @extend_schema(
        request=None,
        responses={200: EarthquakeGetResponseSerializer},
    )
    def get(self, request):
        """
        Return a list of all earthquake data.
        """

        try:
            earthquake = Earthquakes()
            data = earthquake.get_latest_earthquakes()
            serializer = EarthquakeSerializer(data, many=True)
            return Response(Responses.success(serializer.data))
        except Exception as e:
            return Response(Responses.error(str(e)), status=500)
