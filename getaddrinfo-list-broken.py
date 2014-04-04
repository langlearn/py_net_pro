__author__ = 'yang'
# Basic getaddrinfo() not quit right list Example
import sys,socket

result=socket.getaddrinfo(sys.argv[1],None)

counter=0
for item in result:
    print "%-2d: %s" % (counter,item[4])
    counter+=1
