from rest_framework import serializers

from chat_messages.models import Message
from users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):

    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'text', 'created', 'receiver', 'sender')
