# port-crawler
A multithreaded script that determines which ports are open on a remote server, using TCP sockets

# Disclaimer
This script should only be used in an authorized way, as the legality of port scanning might vary depending on country.

# Usage

    python crawler.py <server> <number_of_threads> <option> ... additional arguments
    
## Scanning only a group of chosen ports:

    python crawler.py <server> <number_of_threads> s <list of ports seperated by a comma>
    python crawler.py localhost 2 s 80, 443
    
## Scanning a range of ports

    python crawler.py <server> <number_of_threads> r <lower bound> <upper bound>
    python crawler.py localhost 100 r 80 443
    
## Scanning all ports

    python crawler.py <server> <number_of_threads> a
    python crawler.py localhost 10000 a
    
# Functioning
The script iterates over all possible ports (1 through 65535) and tries to establish a TCP connection. Should the connection succeed, the port will be added to the open ports list and printed late.

A large number of threads is recommended, since establishing a TCP connection is a time consuming task.
