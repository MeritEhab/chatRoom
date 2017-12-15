from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from chat_messages.models import Message
from chat_messages.serializers import MessageSerializer

User = get_user_model()


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
        return Message.get_conversation_messages(self.request.user.id,
                                                 self.kwargs['pk'])


@login_required(login_url='/rest-auth/login')
def user_list(request):

    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'chat_messages/users_list.html', {'users': users})


@login_required(login_url='/rest-auth/login')
def conversation_messages(request, pk):
    pks = [str(request.user.id), str(pk)]
    pks.sort()
    pks = '_'.join(pks)
    messages = Message.get_conversation_messages(request.user.id, pk)
    return render(request, 'chat_messages/messages.html',
                  {'messages': messages, 'pks': pks})
