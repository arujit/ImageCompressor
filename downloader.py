"""
author:james.bondu

simple pyhton script to receive data sent from the server
"""

import sys
import os
import socket
import select
from PIL import Image

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        

    def connect(self):
        host = "127.0.0.1"
        port = 10013
        self.sock.connect((host,port))

    def send(self,data):
        self.sock.send(data)

    def recv(self,BUFFER_SIZE):
        self.sock.recv(BUFFER_SIZE)    
        
    def close(self):
        self.sock.close()
"""
        
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!" 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
""" 

def send_or_receive(client):
    message = "Recv"
    print message
    print "checking to send or receive"
    client.send(message)
    
def receive_data(client,path):
    print client.sock
    socket_list = [sys.stdin,client.sock]
    """
    while True:
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
        for sock in read_sockets:
            # incoming message from remote server
            if sock == client.sock:
                data = sock.recv(1024)
                print data
                if not data:
                    print('\nDisconnected from server')
                    sys.exit()
    """
    
    fp =open(path,"wb")    
    while True:
        data = client.sock.recv(1024)
        if not data:
            print "data finished"
            fp.close()
            ack = True
            #client.close()
            return ack

        #print data
        fp.write(data)
 
    
def data_receive(client):
    client.connect()
    send_or_receive(client)
    path = sys.argv[1]
    if client:
        ack = False
        ack = receive_data(client,path)

        if ack:
            print "Data received"
            img = Image.open(sys.argv[1])
            img.show()
            print "the reduced size: "+ str(os.path.getsize(path))
            client.close()

    return ack
            


if __name__ == "__main__":
    cli = Client()
    ack = data_receive(cli)

    
    if ack:
        print "Data received"
