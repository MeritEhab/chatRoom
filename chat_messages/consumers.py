# handle the basic connections between the client and the server.

import json

from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http

from chat_messages.models import Message

# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message, spk_lpk):
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("chat-%s" % spk_lpk).add(message.reply_channel)


@channel_session_user
def ws_message(message,spk_lpk):
    Group("chat-%s" % spk_lpk).send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.user.username
        }),
    })
    Message.create_mesage(text=message["text"], sender=message.user, channel=spk_lpk)

# Connected to websocket.disconnect


@channel_session
def ws_disconnect(message, spk_lpk):
    Group("chat-%s" % spk_lpk).discard(message.reply_channel)