from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response, decorators, permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from django.http.response import JsonResponse
from django.contrib.auth import get_user_model

from .models import User, UserManager


@api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def create_account(request):
    data = JSONParser().parse(request)
    phone = data.get('phone', None)
    password = data.get('password', None)
    if phone and password:
        if User.objects.filter(phone=phone).exists():
            return JsonResponse({
                        'error': True,
                        'message': "Phone existed"
                    }, status=status.HTTP_400_BAD_REQUEST)
        user = User(phone=phone)
        user.set_password(password)
        user.save()
        return JsonResponse({
                    'error': None,
                    'message': "Success created"
                }, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({
            'error': True,
            'message': "Phone and password are required"
        }, status=status.HTTP_400_BAD_REQUEST)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('phone', 'username')


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


