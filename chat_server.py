"""
необходимо реализовать:
    - прием сообщений от сервера
    - формирование ответа клиенту
    - отправка ответа клиенту
    - принимать параметры командной строки (порт и ip для прослушивания)

"""

import json
from socket import AF_INET, SOCK_STREAM, socket
import sys


class Server:

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self._create_socket()

    def _create_socket(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.listen(5)

    def send_message(self, client, data):
        send_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        client.send(send_data)

    def handle_message(self, request):
        data = json.loads(request.decode('utf-8'))
        if data['action'] == 'presence':
            return {'response': '200', 'alert': 'Успешно'}
        else:
            return {'response': '400', 'alert': 'error'}

    def run(self):
        while True:
            client, addr = self.socket.accept()
            print(f'Принят запрос от {addr}')
            message = client.recv(1024)
            response = self.handle_message(message)
            self.send_message(client, response)
            print(f"Сообщение от клиента - {message.decode('utf-8')}")


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
        host = sys.argv[2]
    except IndexError:
        print('Введите параметры запуска, где первый аргумент - номер порта, второй - хост, например localhost')
    except ValueError:
        print('Введите корректный номер порта')
    server = Server(host, port)
    server.run()
