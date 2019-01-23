from multiprocessing.dummy import Pool as ThreadPool
import socket

def establish_tcp_connection(server, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(server, port)
        return port
    except socket.timeout:
        pass
