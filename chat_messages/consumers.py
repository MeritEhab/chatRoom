# handle the basic connections between the client and the server.

# import json
# from channels import Group
# from channels.auth import channel_session_user, channel_session_user_from_http


# @channel_session_user
# def ws_disconnect(message):
#     Group('users').send({
#         'text': json.dumps({
#             'username': message.user.username,
#             'is_logged_in': False
#         })
#     })
#     Group('users').discard(message.reply_channel)

import json
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http
#from urllib.parse import parse_qs


# @channel_session_user_from_http
# def ws_connect(message):
#     Group('users').add(message.reply_channel)
#     Group('users').send({
#         'text': json.dumps({
#             'username': message.user.username,
#             'is_logged_in': True
#         })
#     })

# Connected to websocket.connect
@channel_session
def ws_connect(message, spk_lpk):
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("users").add(message.reply_channel)
    # Parse the query string
    #params = parse_qs(message.content["query_string"])
    # if b"username" in params:
    #     # Set the username in the session
    #     message.channel_session["username"] = params[b"username"][0].decode("utf8")
    # Add the user to the room_name group

    Group("chat-%s" % spk_lpk).add(message.reply_channel)
    # else:
    # Close the connection.
    # message.reply_channel.send({"close": True})

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
