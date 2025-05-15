import socket
import time 
import threading



print('<<<<server has ben start>>>>')
airport_code=input('Enter the airport code :')

def connection (socka):
    client_name=socka.recv(2048).decode('ascii')

    print('THE CLIENT ',client_name,' IS CONNECTED.')


#while True:

   # request_num=socka.recv(2048).decode('ascii')






#Creating new tcp socket and assign full internet address to it  (ip address and port number )
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_c:
    sock_c.bind(("127.0.0.1" , 49999))

#listening for clients connection 
    sock_c.listen()

#Accepting multiple connection from different client through the while loop 
while True:
    socka , sockname = sock_c.accept()
#Thread that handle clients requests 
t=threading.Thread(target=connection , args=(socka , sockname ))
t.start() 

