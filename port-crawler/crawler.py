from multiprocessing.dummy import Pool as ThreadPool
import socket
import sys

PORTS = [i for i in range(1, 65535)]
SERVER = socket.gethostbyname(sys.argv[1])

def establish_tcp_connection(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(SERVER, port)
        sock.connect((SERVER, port))
        return port
    except socket.timeout:
        pass
    except ConnectionRefusedError:
        pass


def main(argv):
    if len(argv) != 3:
        print("usage: python crawler.py <host> <num_of_threads>")
        exit(1)

    num_threads = int(argv[2])
    pool = ThreadPool(num_threads)
    result = pool.map(establish_tcp_connection, PORTS)

    print("Open ports: ")
    for port in result:
        print(port)

if __name__ == "__main__":
    main(sys.argv[0:])
