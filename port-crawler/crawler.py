from multiprocessing.dummy import Pool as ThreadPool
import socket
import sys

USAGE_MSG = "USAGE: python crawler.py <host> <num_of_threads>"

def panic():
    print(USAGE_MSG)
    exit(1)


def initialize():
    if len(sys.argv) < 3:
        panic()
    server = socket.gethostbyname(sys.argv[1])
    num_threads = int(sys.argv[2])
    return server, num_threads


def main():
    open_ports = []
    ports = [i for i in range(1, 65535)]
    server, num_threads = initialize()
    pool = ThreadPool(num_threads)

    def print_open_ports():
        print("Open ports: ")
        for port in open_ports:
            print(port)

    def establish_tcp_connection(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((server, port))
            open_ports.append(port)
        except OSError:
            pass

    pool.map(establish_tcp_connection, ports)
    print_open_ports()


if __name__ == "__main__":
    main()
