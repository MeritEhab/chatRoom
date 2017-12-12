from django.contrib.auth.models import User
from rest_framework import serializers
from chat_messages.models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','id')

class MessageSerializer(serializers.ModelSerializer):
	
	sender = UserSerializer(read_only=True)

	class Meta:
		model = Message
		fields = ('id', 'text', 'created', 'receiver','sender')

