"""
author:james.bondu

TO-DO
- Use multi Threading for handling of server sending thing ( A separate method to receive images)


Doing
- Multi Threading to both send and receive data
- There must be some way to simply check if its sending or receiving...May be try a separate thread(or main thread )to do the checking first which will invoke a separate 
"""

import socket
from PIL import Image
import os
import sys
from threading import Thread
from SocketServer import ThreadingMixIn
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True



"""
A proper implementation of a python script to create a web socket server and applying different image compression algorithms.
"""
class Communication:
    """Establishing the proper connection"""
    def __init__(self):
        host = "127.0.0.1"
        port = 10013
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((host,port))
        self.server.listen(1)
        print "server set-up finished"
    def close(self):
        self.server.close()

    def send(self,data):
        print "gonna send data"
        self.server.send(data)    


class Server (Thread):
    def __init__ (self,client):
        Thread.__init__(self)
        self.client = client
        print client
        print "New Thread started "+str(Thread)

    
        
    """Constructor for Threaded subclass .... So I can use it to check the initial message eveery time""" 
    def run(self):
        self.message = self.client.recv(4)
        #print self.message

        if self.message == "Recv":
            print "send Data"
            """If client gives signal it's receiving data server has to send data"""
            self.data_send(self.client)
        
        if self.message == "Send":
            print " Data receive"
            """If client is giving signal to receive data then server will send data"""
            self.data_receive(self.client)

    def data_send(self,client):
        self.client = client        
        self.path = "Compressed.jpg"
        print "prepare to send"
        print self.path
        fp = open(self.path,"rb")
        while True:
            self.data = fp.readline(1024)
            if not self.data:
                print "data sent"
                fp.close()
                self.ack = True
                self.client.close()
                break
                
            self.client.send(self.data)


    def data_receive(self,client):
        self.client = client        
        self.path = "Compressed.jpg"
        print self.path
        if self.client:
            self.ack = False
            print "Have you met barney"
            self.ack = self.receive_data(self.client,self.path)

        if self.ack:
            print "have you met Ted?"
            client.close()
            print "Compression Done Bro!!!"

    def receive_data(self,client,file_name):
        self.client = client
        #self.file_name = file_name
        fp = open(file_name,"wb")
        while True:
            self.data = self.client.recv(1024)
            #print self.data
            if not self.data:
                print "data finished"
                fp.close()
                self.compress_image(file_name)
                client.close()
                self.ack = True
                return self.ack

            fp.write(self.data)


    def compress_image(self,path):
        #self.path = path
        """Compression of Images are done in this method"""
        self.img = Image.open(path)
        print self.img.size
        print os.path.getsize(path)
        self.img.save(path,optimize = True,quality = 20)
        print os.path.getsize(path)

"""
        
def compress_image(path):
    img = Image.open(path)
    print img.size
    print os.path.getsize(path)
    img.save(path,optimize = True,quality = 20)
    print os.path.getsize(path)

def receive_data(client,file_name):
    fp = open(file_name,"wb")
    while True:
        data = client.recv(512)
        #print data
        if not data:
            print "data finished"
            fp.close()
            compress_image(file_name)
            ack = False
            return ack

        fp.write(data)

def data_receive(client):
    path = "ironman.jpg"
    if client:
        ack = False
        #receive_data will receive image from clien,write image to disk
        ack = receive_data(client,path)
        if ack:
            print "compression done!!!"

           
        
"""

        
if __name__ == "__main__":
    """basic main method"""
    #data_receive()
    check = Communication()
    threads = []
    while True:
        #Thread(target = send_or_receive(check))
        client,address = check.server.accept()
        newthread = Server(client)
        newthread.start()
        threads.append(newthread)

    for t in threads: 
        t.join() 
        
