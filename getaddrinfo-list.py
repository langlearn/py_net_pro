__author__ = 'yang'
# Basic getaddrinfo() list Example
import sys,socket

# Obtain results for socket.SOCK_STREAM(TCP) only, and put a list
result=socket.getaddrinfo(sys.argv[1],None,0,socket.SOCK_STREAM)

counter=0
for item in result:
    print "%-2d: %s" % (counter,item[4])
    counter+=1
