from socket import socket, AF_INET, SOCK_STREAM
import json

callbacks = {'presence': lambda data: presence(data),
             'msg': lambda data: msg(data)

             }


def create_server(ip: str, port: int) -> socket:
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    return server


def receive_data(server: socket):
    while True:
        client, addr = server.accept()
        print(f'Принят запрос от {addr}')
        while True:
            message = client.recv(1024).decode('utf-8')
            if message == 'q':
                print(f'Соединение с клиентом {addr} закрыто')
                break
            response = handle_data(message)
            print(f'Сообщение от клиента: {message}')
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


def msg(data: dict) -> str:
    pass


if __name__ == '__main__':
    server = create_server('', 8884)
    receive_data(server)
