import json

from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):

    def add_user(self, username="test", email='test@example.com', password='123456789'):
        return User.objects.create(username=username, email=email, password=password)

    def test_user_creation(self):
        user = self.add_user()
        self.assertTrue(isinstance(user, User))


class UserViewTest(TestCase):

    def setUp(self):
        self.sender = User.objects.create_user(username='sender',
                                               email='sender@example.com',
                                               password='123456789')
        self.sender.save()
        self.receiver = User.objects.create_user(username='receiver',
                                                 email='receiver@example.com',
                                                 password='123456789')
        self.receiver.save()

        
    def user_login(self):
        self.client.login(username='sender', email='t1@example.com',
                          password='123456789')
        self.receiver.save()
        self.user = User.objects.create_user(username='user',
                                                 email='user@example.com',
                                                 password='123456789')

    def test_list_messages(self):
        self.user_login()
        action = self.client.get("/home/")
        self.assertEqual(action.status_code, 200)



