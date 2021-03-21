import select
from socket import socket, AF_INET, SOCK_STREAM

ENCODING = "utf-8"


def disconnect_client(sock, all_clients):
    print(f"Клиент {sock.fileno()} {sock.getpeername()} отключился")
    sock.close()
    all_clients.remove(sock)


def read_requests(r_clients, all_clients):
    responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode(ENCODING)
            responses[sock] = data
            #responses[sock].feed_data(data)  # +
        except:
            #disconnect_client(sock, all_clients)  # +
            print("Клиент {} {} отключился".format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        #size = sock.send(clients[sock].data)
        #clients[sock].bytes_sent(size)

        for recv_sock, data in requests.items():
            if sock is recv_sock:
                continue

            try:
                resp = data.encode(ENCODING)
                sock.send(resp)
            except:
                #disconnect_client(sock, all_clients)
                sock.close()
                all_clients.remove(sock)


def mainloop():
    address = ("", 8888)  # заменил 10000 на 8888
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind(address)
        s.listen(5)
        s.settimeout(0.2)
        while True:
            try:
                conn, addr = s.accept()
            except OSError:
                pass
            else:
                print(f"Получен запрос на соединение от {addr}")
                clients.append(conn)
            finally:
                wait = 0
                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], wait)
                except:
                    pass

                requests = read_requests(r, clients)
                write_responses(requests, w, clients)
    finally:
        for sock in clients:
            sock.close()
            s.close()


print("Сервер работает")
mainloop()

