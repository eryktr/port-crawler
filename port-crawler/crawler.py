from multiprocessing.dummy import Pool as ThreadPool
import socket
import sys

USAGE_MSG = "USAGE: python crawler.py <host> <num_of_threads> <option> ... args"
ALL_OPTION = 'a'
SINGLE_OPTION = 's'
RANGE_OPTION = 'r'


def panic():
    print(USAGE_MSG)
    exit(1)


def initialize():

    def initialize_range():
        if len(sys.argv) != 6:
            panic()
        lower = int(sys.argv[4])
        upper = int(sys.argv[5])
        if lower > upper:
            lower, upper = upper, lower
        ports = [port for port in range(lower, upper)]
        return ports

    def initialize_single():
        if len(sys.argv) < 5:
            panic()
        ports = []
        for port in sys.argv[4:]:
            ports.append(int(port))
        return ports

    def initialize_all():
        if len(sys.argv) != 4:
            panic()
        ports = [port for port in range(1, 65535)]
        return ports

    def initialize_ports():
        option = sys.argv[3]
        if option == ALL_OPTION:
            ports = initialize_all()
        elif option == RANGE_OPTION:
            ports = initialize_range()
        elif option == SINGLE_OPTION:
            ports = initialize_single()
        else:
            panic()
        return ports

    if len(sys.argv) < 4:
        panic()
    ports = initialize_ports()
    server = socket.gethostbyname(sys.argv[1])
    num_threads = int(sys.argv[2])
    return server, ports, num_threads


def main():
    open_ports = []
    server, ports, num_threads = initialize()
    pool = ThreadPool(num_threads)

    def print_open_ports():
        if len(open_ports) == 0:
            print("No open ports")

        print("Open ports: ")
        for port in open_ports:
            print(port)

    def establish_tcp_connection(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print(server, port)
            sock.connect((server, port))
            open_ports.append(port)
        except OSError:
            pass

    pool.map(establish_tcp_connection, ports)
    print_open_ports()


if __name__ == "__main__":
    main()
