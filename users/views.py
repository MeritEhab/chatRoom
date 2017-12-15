from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

''' 
ListAPIView
used to read User instances
'''
@login_required(login_url='/rest-auth/login')
def user_list(request):

    users = User.objects.all()
    return render(request, 'chat_messages/users_list.html', {'users': users})

