from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^register/$', views.CreateUserView.as_view(), name='register'),
]