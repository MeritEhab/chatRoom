from django.conf.urls import url
from .views import MessageListCreateView, MessageDetialView


urlpatterns = [
    url(r'^$', MessageListCreateView.as_view(), name='list_create'),
    url(r'^(?P<pk>\d+)/$', MessageDetialView.as_view(),
        name='update_destroy'),
]
