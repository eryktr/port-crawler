from multiprocessing.dummy import Pool as ThreadPool
import socket
import sys


def panic():
    print("usage: python crawler.py <host> <num_of_threads>")
    exit(1)


def initialize():
    try:
        server = socket.gethostbyname(sys.argv[1])
        num_threads = int(sys.argv[2])
        return server, num_threads
    except IndexError:
        panic()


def main():
    OPEN_PORTS = []
    PORTS = [i for i in range(1, 65535)]
    SERVER, NUM_THREADS = initialize()
    POOL = ThreadPool(NUM_THREADS)
    def print_open_ports():
        print("Open ports: ")
        for port in OPEN_PORTS:
            print(port)

    def establish_tcp_connection(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((SERVER, port))
            OPEN_PORTS.append(port)
        except OSError:
            pass

    POOL.map(establish_tcp_connection, PORTS)
    print_open_ports()


if __name__ == "__main__":
    main()
