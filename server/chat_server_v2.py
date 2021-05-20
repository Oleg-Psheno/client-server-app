from socket import socket, AF_INET, SOCK_STREAM
import json
from log.log_config import logger as log

callbacks = {'presence': lambda data: presence(data),
             'msg': lambda data: msg(data),
             'close': lambda data: close(data)
             }


def create_server(ip: str, port: int) -> socket:
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((ip, port))
        server.listen(5)
        log.info(f'Create server at "{ip}":{port}')
    except OSError as e:
        log.error(f'Error - {e}')
        exit(2)
    return server


def receive_data(server: socket):
    while True:
        client, addr = server.accept()
        # print(f'Принят запрос от {addr}')
        log.info(f'Принят запрос от {addr}')
        while True:
            message = client.recv(1024).decode('utf-8')
            response = handle_data(message)
            if response == 'q':
                # print(f'Соединение с клиентом {addr} закрыто')
                log.info(f'Соединение с клиентом {addr} закрыто')
                break
            # print(f'Сообщение от клиента: {message}')
            log.info(f'Сообщение от клиента: {message}')
            client.send(response.encode('utf-8'))


def handle_data(message: str) -> str:
    data = json.loads(message)
    response = callbacks[data["action"]](data)
    return response


def presence(data: dict) -> str:
    user = data['user']['account_name']
    response = {'response': '200', 'alert': 'Успешно'}
    return json.dumps(response, ensure_ascii=False)


def send_message_to_client(client: socket, message: str) -> None:  # TODO: возможно она должна возвращать ответ
    client.send(message.encode('utf-8'))


def msg(data: dict) :
    return json.dumps({'response': '200', 'alert': 'Успешно'}, ensure_ascii=False)

def close(data):
    return 'q'


if __name__ == '__main__':
    server = create_server('', 8885)
    receive_data(server)
