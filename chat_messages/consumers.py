# handle the basic connections between the client and the server.

import json
from channels import Group
from channels.sessions import channel_session

# Connected to websocket.connect
@channel_session
def ws_connect(message, spk_lpk):
    message.reply_channel.send({"accept": True})
    Group("users").add(message.reply_channel)
    Group("chat-%s" % spk_lpk).add(message.reply_channel)


# Connected to websocket.receive
@channel_session
def ws_message(message, spk_lpk):
    print '#' * 100
    Group("chat-%s" % spk_lpk).send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.channel_session["username"],
        }),
    })

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message, spk_lpk):
    Group("chat-%s" % spk_lpk).discard(message.reply_channel)
