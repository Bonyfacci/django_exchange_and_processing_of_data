from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import PurchaseCheck
from .serializers import PurchaseCheckSerializer


class PurchaseCheckCreateView(generics.CreateAPIView):
    queryset = PurchaseCheck.objects.all()
    serializer_class = PurchaseCheckSerializer
    permission_classes = [AllowAny]
