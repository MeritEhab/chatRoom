from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
