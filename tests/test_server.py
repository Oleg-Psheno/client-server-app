import socket
import json
from chat_server_v2 import create_server, handle_data, presence, msg

def test_create_server():
    server = socket.socket()
    server.bind(('',8001))
    assert type(create_server('',7000)) == type(server)

def test_presence():
    assert presence({'action':'presence','user':{'account_name':'Pit'}}) == json.dumps({'response': '200', 'alert': 'Успешно'}, ensure_ascii=False)

def test_handle_data():
    callbacks = {'presence': lambda data: presence(data),
                 'msg': lambda data: msg(data)}
    message = json.dumps({'action':'presence','user':{'account_name':'Pit'}})
    assert handle_data(message) == json.dumps({'response': '200', 'alert': 'Успешно'},ensure_ascii=False)