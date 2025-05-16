import socket
import requests 
import threading
import json



print('<<<<server has ben start>>>>')
airport_code=input('Enter the airport code :')

#creating the parameters to pass thim to api.
parameters= {
    'access_key': 'b5839f51c23a1a1f4cd15a24d5bd17bc' ,# api access key from the website acount.
    'arr_icao':airport_code,
    'limit':100  #the limit is by defult is 100.
}

# To get the response for the website with the parameters we set. 
api_result= requests.get('https://api.aviationstack.com/v1/flights',parameters)

#for handeling any error form api_result.
if api_result.status_code !=200:
    raise ApiError('GET/TASKS/ {}'.format(resp.status_code))

# svaing the data recievd in file.
with open ()as P1:
    PP1=requests.get('https://api.aviationstack.com/v1/flights',parameters)
    Jresults =json.dumps(api_result.json(),P1, indent=1)

def connection (socka):
    client_name=socka.recv(2048).decode('ascii')

    print('THE CLIENT ',client_name,' IS CONNECTED.')

    while True:
        request_num=socka.recv(2048).decode('ascii') # type: ignore


#creating the socket and asssign IP and port number.
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_2:
    sock_2.bind(('127.0.0.1',499999))

    sock_2.listen()

#creating the thread.
t1=threading.Thread(name='thread 1')

#t1.start()

