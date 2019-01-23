# port-crawler
A multithreaded script that determines which ports are open on a remote server, using TCP sockets

# Usage

    python crawler.py <server> <number_of_threads>
    
# Functioning
The script iterates over all possible ports (1 through 65535) and tries to establish a TCP connection. Should the connection succeed, the port will be added to the open ports list and printed late.

A large number of threads is recommended, since establishing a TCP connection is a time consuming task.
