from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from chat_messages.models import Message
from chat_messages.serializers import MessageSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Message.objects.filter(Q(sender=self.request.user) |
                                          Q(receiver=self.request.user))
        return queryset

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageDetialView(generics.RetrieveUpdateDestroyAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Message.objects.filter(sender=self.request.user)
        return queryset


class ConversationMessageList(generics.ListAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Message.objects.filter((Q(sender=self.request.user) & Q(
            receiver=self.kwargs['pk'])) | (Q(sender=self.kwargs['pk']) & Q(
                receiver=self.request.user)))
