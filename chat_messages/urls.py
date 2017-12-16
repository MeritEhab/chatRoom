from django.conf.urls import url
from chat_messages.views import (MessageListCreateView, MessageDetialView,
                                 ConversationMessageList,
                                 conversation_messages)

urlpatterns = [
    url(r'^$', MessageListCreateView.as_view(),
        name='list_create'),
    url(r'^(?P<pk>\d+)/$', MessageDetialView.as_view(),
        name='update_destroy'),
    url(r'^conversation_list/(?P<pk>\d+)/$', ConversationMessageList.as_view(),
        name='conversation'),
    url(r'^conversation/(?P<pk>\d+)/$', conversation_messages,
        name='conversation'),

]
