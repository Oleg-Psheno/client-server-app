from socket import socket, AF_INET, SOCK_STREAM


def mainloop(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)
    while True:


        msg = input('Введите сообщение: ')
        if msg == 'q':
            break
        sock.send(msg.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        print(data)
    sock.close()


if __name__ == '__main__':
    mainloop(('',8888))
