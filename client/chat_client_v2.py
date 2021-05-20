import json
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime
from log.log_config import logger as log

account_name = 'Oleg'

def create_client(ip: str, port: int) -> socket:
    log.info('Тест от клиента')
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ip, port))
    except OSError as e:
        log.error(e)
    return client


def send_message(data: dict, client: socket) -> None:
    message = json.dumps(data, ensure_ascii=False)
    client.send(message.encode('utf-8'))

def get_dict_message(msg, reciever):
    return {'action':'msg',
            'message': msg,
            'time': str(datetime.now()),
            'to': reciever,
            'from': account_name,
            'encoding':'utf-8',
            }

def get_presence_message(account_name):
    return {'action': 'presence',
            'time': str(datetime.now()),
            'type': 'status',
            'user': {'account_name': account_name,
                     'status': 'Enable'}
            }


if __name__ == '__main__':

    client = create_client('', 8885)
    send_message(get_presence_message('oleg'), client)
    log.info(client.recv(1024).decode('utf-8'))
    while True:

        msg = input('Enter your message: \n')
        send_message(get_dict_message(msg,'Peter'), client)
        if msg == 'q':
            break
        message_from_server = client.recv(1024)
        print(message_from_server.decode('utf-8'))
    client.close()
