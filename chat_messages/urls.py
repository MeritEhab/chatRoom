from django.conf.urls import url
from .views import MessageList


urlpatterns = [
    url(r'^$',MessageList.as_view(),name='messages_list'),
]

