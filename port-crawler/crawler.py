from multiprocessing.dummy import Pool as ThreadPool
import socket
import sys


def panic():
    print("usage: python crawler.py <host> <num_of_threads>")
    exit(1)


PORTS = [i for i in range(1, 65535)]
OPEN_PORTS = []

try:
    SERVER = socket.gethostbyname(sys.argv[1])
    NUM_THREADS = int(sys.argv[2])
except IndexError:
    panic()

POOL = ThreadPool(NUM_THREADS)


def establish_tcp_connection(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER, port))
        OPEN_PORTS.append(port)
    except OSError:
        pass


def main(argv):

    def print_open_ports():
        print("Open ports: ")
        for port in OPEN_PORTS:
            print(port)

    POOL.map(establish_tcp_connection, PORTS)
    print_open_ports()



if __name__ == "__main__":
    main(sys.argv)
