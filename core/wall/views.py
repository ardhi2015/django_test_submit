from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import WallLikes, WallPost
from .serializers import WallLikeSerializer, WallPostSerializer


class WallView(viewsets.ModelViewSet):
    queryset = WallPost.objects.all()
    serializer_class = WallPostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class WallLikeView(viewsets.ModelViewSet):
    queryset = WallLikes.objects.all()
    serializer_class = WallLikeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
