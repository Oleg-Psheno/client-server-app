import json
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime


def create_client(ip: str, port: int) -> socket:
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((ip, port))
    return client


def send_message(data: dict, client: socket) -> None:
    message = json.dumps(data, ensure_ascii=False)
    client.send(message.encode('utf-8'))


def get_presence_message(account_name):
    return {'action': 'presence',
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': 'status',
            'user': {'account_name': account_name,
                     'status': 'Enable'}
            }


if __name__ == '__main__':

    client = create_client('', 8884)
    send_message(get_presence_message('oleg'), client)
    print(client.recv(1024).decode('utf-8'))
    while True:

        msg = input('Enter your message: \n')
        send_message(msg, client)
        if msg == 'q':
            break
        message_from_server = client.recv(1024)
        print(message_from_server.decode('utf-8'))
    client.close()
