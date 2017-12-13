from django.conf.urls import url

from users.views import UsersList

urlpatterns = [
    url(r'^users$', UsersList.as_view(), name='list_users')
]
