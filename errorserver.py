__author__ = 'Yang'
#Server With Error Handling
import socket,traceback

host=''
port=51423

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while 1:
    try:
        clientsock,clientaddr=s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    try:
        print "Got connection from",clientsock.getpeername()
        # Process the request here
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()

    # Close the connection
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
