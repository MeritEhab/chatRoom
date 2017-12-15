from django.apps import AppConfig


class MessagesConfig(AppConfig):
    name = 'chat_messages'

    def ready(self):
        import chat_messages.signals
