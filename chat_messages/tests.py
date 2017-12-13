import json

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient


from chat_messages.models import Message
from chat_messages.serializers import MessageSerializer


class MessagesModelTest(TestCase):

    def add_message(self, text="Message 1", sender=User.objects.get(id=1),
                    receiver=User.objects.get(id=1)):
        return Message.objects.create(text=text, sender=sender,
                                      receiver=receiver)

    def test_message_creation(self):
        message = self.add_message()
        self.assertTrue(isinstance(message, Message))


class MessagesViewTest(TestCase):

    def setUp(self):
        self.sender = User.objects.create_user(username='sender',
                                               email='sender@example.com',
                                               password='123456789')
        self.sender.save()
        self.receiver = User.objects.create_user(username='receiver',
                                                 email='receiver@example.com',
                                                 password='123456789')
        self.receiver.save()

        # self.message1 = Message.objects.create(text='Hi', sender=self.sender,
        #                                        receiver=self.receiver,
        #                                        created="2017-12-11T10:26:58.111181Z")
        # self.message2 = Message.objects.create(text='Hello', sender=self.sender,
        #                                        receiver=self.receiver,
        #                                        created="2017-12-11T10:30:58.111181Z")
        self.client = APIClient()
        self.client.force_authenticate(user=self.sender)

        self.message_data = {'text': 'hi', 'sender': self.sender.id,
                             'receiver': self.receiver.id, 'created': '2017-12-11T10:30:58.111181Z'}
        self.response = self.client.post(
            reverse('list_create'),
            self.message_data,
            format="json")

    # def user_login(self):
    #     self.client.login(username='sender', email='t1@example.com',
    #                       password='123456789')

    # def test_list_messages(self):
    #     response = client.get_queryset(reverse('list_create'))
    #     # get data from db
    #     messages = Message.objects.filter(sender=self.sender,
    #                                       receiver=self.receiver)
    #     serializer = MessageSerializer(messages)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_create_a_message(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get('/messages/', kwargs={'pk': 1}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_Message(self):
        message = Message.objects.get(id=1)
        response = self.client.get(
            '/message/',
            kwargs={'pk': message.id}, format="json")
        print type(response)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, message)

    def test_api_can_update_Message(self):
        message = Message.objects.get(id=1)
        res = self.client.put(
            reverse('update_destroy', kwargs={
                "id": message.id,
                "text": "Hola Hola ",
                "created": "2017-12-13T16:23:24.101925Z",
                "receiver": message.receiver.id,
                "sender": message.sender
            }),
            format='json'
        )
        print res
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        message = Message.objects.get(id=1)
        print self.client
        response = self.client.delete(
            reverse('update_destroy', kwargs={'pk': message.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
