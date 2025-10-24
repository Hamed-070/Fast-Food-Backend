from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Food

class CustomUserSerializer(TokenObtainPairSerializer):
    def validate(self , attrs):
        data = super().validate(attrs)
        data['user'] = {
            'username': self.user.username
        }
        return data

class FoodSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'








