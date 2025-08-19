from .serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Food
from .serializers import FoodSerializerView

class CustomUserView(TokenObtainPairView):
    serializer_class = CustomUserSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializerView
    permission_classes = [AllowAny]


