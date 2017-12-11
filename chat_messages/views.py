from chat_messages.serializers import MessageSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from chat_messages.models import Message


class MessageListCreateView(generics.ListCreateAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Message.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageDetialView(generics.RetrieveUpdateDestroyAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Message.objects.filter(user=self.request.user)
        return queryset
