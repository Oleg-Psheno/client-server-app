import select
from socket import socket, AF_INET, SOCK_STREAM

def create_socket(address):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.5)
    return sock

def read(r,all):
    responses = {}
    for sock in r:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
            if not data:
                raise Exception
        except:
            print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
            all.remove(sock)
        else:
            print(f'Клиент {sock.fileno()} написал {data}')
    return responses

def send(requests, w, all):
    for sock in w:
        if sock in requests:
            try:
                text = f'Клиент {sock.fileno()} - сообщение -  {requests[sock]}'
                response = text.encode('utf-8')
                sock.send(response)
            except Exception as e:
                print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился, исключение - {e}')
                sock.close()
                all.remove(sock)

def mainloop(address):
    s = create_socket(address)
    clients = []
    while True:
        try:
            conn,addr = s.accept()
        except OSError as e:
            pass
            # print(f'Исключение 1 OSError {e}')
        else:
            print(f'Получен запрос от клиента {str(addr)}')
            clients.append(conn)
        finally:
            wait = 1
            r = []
            w = []
            try:
                r,w,e = select.select(clients,clients,[],wait)
            except Exception as e:
                print(f'Исключение 2 {e}')
            requests = read(r,clients)
            if requests:
                send_2(requests,w,clients)


def send_2(requests,w,all):
    for mes in requests:
        for sock in all:
            text = f'Клиент {mes.fileno()} - сообщение -  {requests[sock]}'
            response = text.encode('utf-8')
            sock.send(response)


if __name__ == '__main__':
    mainloop(('',8888))
