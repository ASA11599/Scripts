import socket
import typing
import threading

def get_tcp_connections(host: str = "127.0.0.1", port: int = 8080) -> typing.Generator[socket.socket, None, None]:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setblocking(False)
        s.bind((host, port))
        s.listen()
        for _ in range(5):
            c: socket.socket = s.accept()[0]
            with c: yield c

def handle_connection(c: socket.socket) -> None:
    print(c)

def main() -> None:
    connection_threads: set[threading.Thread] = set()
    for c in get_tcp_connections("192.168.64.15"):
        t: threading.Thread = threading.Thread(target=handle_connection, args=(c,))
        connection_threads.add(t)
        t.start()
    for t in connection_threads:
        t.join()

if __name__ == "__main__":
    main()
