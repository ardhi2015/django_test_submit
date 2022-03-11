from core.utils.responses import Responses
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
from drf_spectacular.utils import extend_schema
from rest_framework import parsers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, UserResponseSerializer, UserSerializer


@api_view()
@schema(None)
def hello_world(request):
    return Response({"message": "Hello, world!"})


class LoginView(ObtainAuthToken):
    parser_classes = (parsers.JSONParser,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username, password = serializer.data.values()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    Responses.success(
                        {"token": token.key, "user_id": user.pk},
                        message="Login successful",
                    ),
                )
            else:
                return Response(Responses.error("User not found"), status=400)
        else:
            return Response(Responses.error(str(serializer.errors)), status=400)


class RegisterView(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={201: UserResponseSerializer},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(Responses.success(serializer.data), status=201)
            except IntegrityError as e:
                print(f"Error: {e}")
                return Response(Responses.error("User already exists"), status=400)
        return Response(Responses.error(str(serializer.errors)), status=400)
