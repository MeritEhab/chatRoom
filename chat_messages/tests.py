import json

from django.test import TestCase
from django.contrib.auth.models import User

from chat_messages.models import Message

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

        self.message1 = Message.objects.create(text='Hi', sender=self.sender,
                                               receiver=self.receiver,
                                               created="2017-12-11T10:26:58.111181Z")
        
    def user_login(self):
        self.client.login(username='sender', email='t1@example.com',
                          password='123456789')

    def test_list_messages(self):
        self.user_login()
        action = self.client.get("/message/")
        self.assertEqual(action.status_code, 200)
        self.assertEqual(len(json.loads(action.content)), 1)

    def test_send_message(self):
        self.user_login()
        new_messge ={
            'text':'Hello',
            'sender':self.sender,
            'receiver':self.receiver.id
            }
        action = self.client.post("/message/", new_messge)
        respone = json.loads(action.content)
        action_list = self.client.get("/message/")
        self.assertEqual(action.status_code, 201)
        self.assertEqual(len(json.loads(action_list.content)), 2)
        self.assertEqual(respone['text'], new_messge['text'])
        self.assertEqual(respone['receiver'], new_messge['receiver'])

    def test_update_message(self):
        self.user_login()
        update_message = {
        'text':'Thankyou',
        'receiver': self.receiver.id
        }
        action = self.client.put("/message/%s/" % self.message1.id,
            json.dumps(update_message), content_type="application/json")
        action_list = self.client.get("/message/%s/" % self.message1.id)
        respone = json.loads(action_list.content)
        self.assertEqual(action.status_code, 200)
        self.assertEqual(respone['text'], update_message['text'])
        

    def test_delete_message(self):
        self.user_login()
        action = self.client.delete("/message/%s/" % self.message1.id)
        self.assertEquals(action.status_code, 204)

class ConversationTest(TestCase):

    def setUp(self):
        self.sender = User.objects.create_user(username='sender',
                                               email='sender@example.com',
                                               password='123456789')
        self.sender.save()
        self.receiver = User.objects.create_user(username='receiver',
                                                 email='receiver@example.com',
                                                 password='123456789')
        self.receiver.save()
        self.user = User.objects.create_user(username='user',
                                                 email='user@example.com',
                                                 password='123456789')
        self.user.save()

        self.message1 = Message.objects.create(text='Hi', sender=self.sender,
                                               receiver=self.receiver,
                                               created="2017-12-11T10:26:58.111181Z")
        self.message2 = Message.objects.create(text='Hi', sender=self.receiver,
                                               receiver=self.sender,
                                               created="2017-12-11T10:35:58.111181Z")
        self.message3 = Message.objects.create(text='Hi', sender=self.sender,
                                               receiver=self.user,
                                               created="2017-12-11T10:26:58.111181Z")
    def user_login(self):
        self.client.login(username='sender', email='t1@example.com',
                          password='123456789')

    def test_list_conversation(self):
        self.user_login()
        action = self.client.get("/message/conversation_list/%s/"% self.receiver.id)
        self.assertEqual(action.status_code, 200)
        self.assertEqual(len(json.loads(action.content)), 2)

