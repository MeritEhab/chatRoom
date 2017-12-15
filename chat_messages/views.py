from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from chat_messages.models import Message
from chat_messages.serializers import MessageSerializer

''' 
ListCreateAPIView
used to read-write Message instances
'''

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

'''
RetriveUpdateDestroyAPIView
used to read-write-delete a single Message instance.
'''
class MessageDetialView(generics.RetrieveUpdateDestroyAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Message.objects.filter(sender=self.request.user)
        return queryset

''' 
List Messages of a coversation between 2 users 
get_conversation_messages method:
it retrives conversation messages by filtering message accorrding
to a condition that states the a message has to be sent or
 received by any of the 2 users 
'''
class ConversationMessageList(generics.ListAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Message.get_conversation_messages(self.request.user.id,
                                                 self.kwargs['pk'])

'''
Method use to do the sme functionalty as the upove class, 
but also uses a template to render 
'''
@login_required(login_url='/rest-auth/login')
def conversation_messages(request, pk):
    pks = [str(request.user.id), str(pk)]
    pks.sort()
    pks = '_'.join(pks)
    messages = Message.get_conversation_messages(request.user.id, pk)
    return render(request, 'chat_messages/messages.html',
                  {'messages': messages, 'pks': pks})
