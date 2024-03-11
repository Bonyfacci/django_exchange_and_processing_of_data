from django.urls import path

from .apps import ConsumerConfig
from .views import PlaceListCreateView, PlaceDetailView, OverallAnalyticsView

app_name = ConsumerConfig.name

urlpatterns = [
    path('api/places/', PlaceListCreateView.as_view(), name='place-list-create'),
    path('api/places/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
    path('api/analytics/', OverallAnalyticsView.as_view(), name='overall-analytics'),
]
