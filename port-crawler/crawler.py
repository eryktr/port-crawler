from multiprocessing.dummy import Pool as ThreadPool
import socket
import sys

PORTS = [i for i in range(1, 65535)]
SERVER = socket.gethostbyname(sys.argv[1])
OPEN_PORTS = []


def establish_tcp_connection(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER, port))
        OPEN_PORTS.append(port)
    except OSError:
        pass


def main(argv):
    def initialize():
        num_threads = int(argv[2])
        pool = ThreadPool(num_threads)
        return pool

    def print_open_ports():
        print("Open ports: ")
        for port in OPEN_PORTS:
            print(port)

    def panic():
        print("usage: python crawler.py <host> <num_of_threads>")
        exit(1)

    if len(argv) != 3:
        panic()
    pool = initialize()
    result = pool.map(establish_tcp_connection, PORTS)
    print_open_ports()



if __name__ == "__main__":
    main(sys.argv[0:])
