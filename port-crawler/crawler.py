from multiprocessing.dummy import Pool as ThreadPool
import socket

PORTS = [i for i in range(0, 65535)]

def establish_tcp_connection(server, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(server, port)
        return port
    except socket.timeout:
        pass


def main(argv):
    if len(argv) != 3:
        print("usage: python crawler.py <host> <num_of_threads>")
        exit(1)

    host = socket.gethostbyname(argv[1])
    num_threads = int(argv[3])

if __name__ == "__main__":
