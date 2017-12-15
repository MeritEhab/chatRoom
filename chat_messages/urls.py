from django.conf.urls import url
from chat_messages.views import (MessageListCreateView, MessageDetialView,
                                 ConversationMessageList,
                                 conversation_messages)

urlpatterns = [
    url(r'^$', MessageListCreateView.as_view(),
        name='api/list_create'),
    url(r'^api/(?P<pk>\d+)/$', MessageDetialView.as_view(),
        name='update_destroy'),
    url(r'^api/conversation/(?P<pk>\d+)/$', ConversationMessageList.as_view(),
        name='api_conversation'),
    url(r'^conversation/(?P<pk>\d+)/$', conversation_messages,
        name='conversation'),

]
