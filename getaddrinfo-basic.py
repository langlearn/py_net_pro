__author__ = 'yang'
# Basic getaddressinfo() basic example
import sys, socket

result=socket.getaddrinfo(sys.argv[1],None)
print result[0][4]
