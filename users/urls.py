from django.conf.urls import url

from users.views import user_list

urlpatterns = [
    url(r'^$', user_list, name='list_users')
]
