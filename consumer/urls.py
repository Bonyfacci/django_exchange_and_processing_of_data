from django.urls import path

from producer.apps import ProducerConfig
from .views import PlaceListCreateView, PlaceDetailView

app_name = ProducerConfig.name

urlpatterns = [
    path('places/', PlaceListCreateView.as_view(), name='place-list-create'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
]
