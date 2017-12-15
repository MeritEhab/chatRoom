from channels.routing import route
from chat_messages.consumers import ws_connect, ws_message, ws_disconnect


# def message_handler(message):
#     print message.content
#     print(message['text'])
# channel_routing = [
#     route('websocket.connect', ws_connect),
#     route('websocket.disconnect', ws_disconnect),
#     route("websocket.send", message_handler)
# ]


channel_routing = [
    route("websocket.connect", ws_connect, path=r"^/(?P<spk_lpk>[0-9_]+)/$"),
    route("websocket.receive", ws_message, path=r"^/(?P<spk_lpk>[0-9_]+)/$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/(?P<spk_lpk>[0-9_]+)/$"),
]
