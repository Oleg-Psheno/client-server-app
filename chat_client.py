'''
реализовать:
    - формирование presence - сообщения
    - отправление сообщений серверу
    - получение ответа от сервера
    - разбор сообщений сервера
    - прием параметров командной строки
'''

import json
from socket import socket, AF_INET, SOCK_STREAM, gaierror, error
from datetime import datetime
import sys


class Client:

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.account_name = 'Олег'
        self._create_socket()

    def _create_socket(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((self.ip, self.port))

    def get_time(self):
        return str(datetime.timestamp(datetime.now()))

    def _send_data(self, data):
        send_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.socket.send(send_data)
        response = json.loads(self.socket.recv(1024).decode('utf-8'))
        return response

    def get_presence_message(self):
        return {'action': 'presence',
                'time': self.get_time(),
                'type': 'status',
                'user': {'account_name': self.account_name,
                         'status': 'Enable'}
                }

    def run(self):
        response = self._send_data(self.get_presence_message())
        self.response_handler(response)

    def response_handler(self, response):
        if response['response'] == '200':
            print(f'Соединение с сервером установлено, {response["alert"]}')


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
        host = sys.argv[2]
    except IndexError:
        print('Введите параметры запуска, где первый аргумент - номер порта, второй - хост, например localhost')
    except ValueError:
        print('Введите корректный номер порта')

    client = Client(host, port)
    client.run()
