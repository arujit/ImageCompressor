# ImageCompressor
## A simple Socket client-server arrangement for getting Images and compress them and sending them to the downloader.

### Scripts - 
I have written the scripts to remain somewhat in upload,download system. There are two clients script for uploading and downloading images respectively.
And a server script that gets the client requests first and in accordance receive Image and Compress it or send image.
#### Server.py - 
It the script for server. It always create a thread for handling Client request. It first receives a message from Clients denoting either client is sending or want to receive images from Server.
If it finds client want to send Image then it creates a separate Thread for receiving the image sent by client(Sender) and Compress the image and stores in Compressed.jpg file."Compressed.jpg" is like a temporary Image buffer that stores the Image Compressed by the Server.
If Server finds out that client(Downloader) wants to receive Compressed Image, then it simlpy sends the image stored in Image buffer "Compressed.jpg"

#### Sender.py - 
Use - python Sender.py [file path of the Image that is to be sent]
first sends a 4 byte "Send" Message denoting it is going to send image . Then simply open the Image in denoted path and sends to Sever in 512bytes byte code format.Typically the Image to be sent will be in "Sending" Directory.

#### Downloader.py -
Use - python downloader.py [file path to write downloaded Image]
First sends a 4 byte "Recv" Message string denoting that it is going to receive Image. That after server completing sending Image it simply writes to the denoted path.
