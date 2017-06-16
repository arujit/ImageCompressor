
"""
author : james.bondu
TO-DO : 
- base 64 encoding
- separate script to retrive image from the server
"""
import sys
import os
import socket


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self):
        host = "127.0.0.1"
        port = 10013
        self.sock.connect((host,port))

    def send(self,data):
        self.sock.send(data)

    def close(self):
        self.sock.close()

def send_or_receive(client):
    message = "Send"
    print message
    print "checking send or receive"
    client.send(message)
    #message = client.recv(1024)
    #print message
    #client.close()
        
def send_data(client , path):
    client.connect()
    """
    how the server know that client is sending or receiving
    """
    send_or_receive(client)
    #client.connect()
    print path
    fp = open (path,"rb")
    #print client
    #client.connect(10006)
    
    while True:
        """sending 512 bytes of data in a go"""
        data = fp.readline(1024)
        #print "data present bro"
        #print data
        if not data:
            print "send data!!!"
            client.close()
            fp.close()
            ack = True
            break
        client.send(data)
    return ack
        
if __name__ == "__main__":
    file_name = sys.argv[1]
    #fp = open(file_name,"rb")
    print "starting the sending process!!!"

    cli = Client()
    ack = send_data(cli,file_name)

    if ack :
        print "Data sending complete"
        
