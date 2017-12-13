from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
