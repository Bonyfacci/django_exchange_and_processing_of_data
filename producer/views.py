from rest_framework import generics
from .models import PurchaseCheck
from .serializers import PurchaseCheckSerializer


class PurchaseCheckCreateView(generics.CreateAPIView):
    queryset = PurchaseCheck.objects.all()
    serializer_class = PurchaseCheckSerializer
