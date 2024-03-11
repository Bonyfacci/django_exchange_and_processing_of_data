from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Place, OverallAnalytics
from .serializers import PlaceSerializer, OverallAnalyticsSerializer


class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [AllowAny]


class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]


class OverallAnalyticsView(generics.ListAPIView):
    queryset = OverallAnalytics.objects.all()
    serializer_class = OverallAnalyticsSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = OverallAnalytics.objects.all().last()
        serializer = OverallAnalyticsSerializer(queryset)
        return Response(serializer.data)

