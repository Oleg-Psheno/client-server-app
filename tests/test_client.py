from datetime import datetime
import socket
import json
from chat_client_v2 import create_client, get_presence_message

def test_create_client():
    server = socket.socket()
    server.bind(('',7001))
    server.listen(5)

    assert type(create_client('',7001)) == type(server)

def test_get_presence_message():
    responce = {'action': 'presence',
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': 'status',
            'user': {'account_name': 'Oleg',
                     'status': 'Enable'}
            }
    assert get_presence_message('Oleg') == responce
