from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import response, decorators, permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers

from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

from .serializers import UserSerializer


from .models import User, UserManager

from .constants import USER_IMAGE_FIELD


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


@api_view(['GET'])
@decorators.permission_classes([permissions.AllowAny])
def get_users(request):
    limit = request.query_params.get('limit', 10)
    offset = request.query_params.get('offset', 0)

    users = User.objects.all()[int(offset):(int(offset) + int(limit))]
    users_serializer = UserSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False)


class UserCurrent(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request, format=None):
        user_data = model_to_dict(request.user)
        for field in USER_IMAGE_FIELD:
            if field in user_data:
                del(user_data[field])
        for key in request.data:
            if request.data[key]:
                user_data[key] = request.data[key]
        serializer = UserSerializer(request.user, data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserById(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self, pk):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        user_data = model_to_dict(user)
        for field in USER_IMAGE_FIELD:
            if field in user_data:
                del (user_data[field])
        for key in request.data:
            if request.data[key]:
                user_data[key] = request.data[key]
        serializer = UserSerializer(user, data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



