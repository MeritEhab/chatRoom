from django.conf.urls import url
from chat_messages.views import (MessageListCreateView, MessageDetialView,
                                 ConversationMessageList, user_list,
                                 conversation_messages)


urlpatterns = [
    url(r'^$', MessageListCreateView.as_view(),
        name='list_create'),
    url(r'^(?P<pk>\d+)/$', MessageDetialView.as_view(),
        name='update_destroy'),
    url(r'^api/conversation/(?P<pk>\d+)/$', ConversationMessageList.as_view(),
        name='api_conversation'),
    url(r'^user_list$', user_list, name='user_list'),
    url(r'^conversation/(?P<pk>\d+)/$', conversation_messages,
        name='conversation'),

]
