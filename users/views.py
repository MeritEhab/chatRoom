from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from users import Serializers
# Create your views here.

class CreateUserView(generics.CreateAPIView):

	model = get_user_model()
	permission_class = (permissions.AllowAny,)
	serializer_class = Serializers.UserSerializer