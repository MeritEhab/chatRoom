from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    '''
    this method get the messages of the conversation in decending order
    based on created time and it gets the last 10 messages the -1 to 
    reverse the order on displaying  
    '''
    @classmethod
    def get_conversation_messages(cls, frst_user_id, scnd_user_id):
        return Message.objects.filter((Q(sender=frst_user_id) & Q(
            receiver=scnd_user_id)) | (Q(sender=scnd_user_id) & Q(
                receiver=frst_user_id))).order_by('-created')[:10][::-1]
        
    @classmethod
    def create_mesage(cls, text, sender, channel):
    	pks = channel.split('_')
    	pks.remove(str(sender.id))
    	receiver_pk = pks[0]
    	receiver = User.objects.get(id=receiver_pk)
    	Message.objects.create(text=text, sender=sender, receiver=receiver)