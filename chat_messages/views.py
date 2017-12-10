from django.contrib.auth.models import User
from chat_messages.serializers import MessageSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from chat_messages.models import Message


class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
