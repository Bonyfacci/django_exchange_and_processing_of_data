from django.urls import path

from .apps import ProducerConfig
from .views import PurchaseCheckCreateView

app_name = ProducerConfig.name

urlpatterns = [
    path('api/checks/', PurchaseCheckCreateView.as_view(), name='purchase-check-create'),
]
