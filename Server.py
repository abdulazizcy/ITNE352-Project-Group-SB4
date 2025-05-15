import socket
import time 
import threading



print('<<<<server has ben start>>>>')
airport_code=input('Enter the airport code :')

def connection (socka):
    client_name=socka.recv(2048).decode('ascii')

    print('THE CLIENT ',client_name,' IS CONNECTED.')


while True:

    request_num=socka.recv(2048).decode('ascii')