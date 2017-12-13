from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from chat_messages.serializers import UserSerializer


class UsersList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
