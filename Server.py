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
with open ('group_SB4.json','w')as P1:
    PP1=requests.get('https://api.aviationstack.com/v1/flights',parameters)
    Jresults =json.dumps(PP1.json(),P1, indent=1)
    json.dump(PP1.json(),P1,indent=1)




def connection (socka):
    client_name=socka.recv(2048).decode('ascii') # to recive the clints name for clints side.
    print('THE CLIENT ',client_name,' IS CONNECTED.')

    while True:
        i=0
        request_num=socka.recv(2048).decode('ascii') # to recive the requst form the clients.
        #to loade the data from the file.
        with open ('PP1.josn','r') as P1:
            P2=json.load(P1)

            #creating if statment to chose the data that user want to see and save thime in new parameters.
            # to print the all arived flights.
            if request_num=="1":
                print('clinet name: ',client_name,'\n''requst type :arrived flights')
                landed=''  
                for flights in P1['data']:
                    if (flights['flight_status'=='landed']):
                        landed+='Flight IATA code: ',flights['flight']['iataNumber']+'\n'           #Returns the IATA number of the flight.
                        landed+='Departure airport name: ',flights['departure']['airport']+'\n'     #Returns the name of the departure airport.
                        landed+='Arrival time: ',flights['arrival']['time']+'\n'                    #Returns the Arrival time.
                        landed+='Arrival terminal number: ',flights['arrival']['terminal']+'\n'     #Returns the arrival terminal.
                        landed+='Arrival gate: ',flights['flight']['gate']+'\n'                     #Returns the arrival gate.
                print(landed)
            # to print the all delayed flights.
            elif request_num =='2':
                print('clinet name: ',client_name,'\n''requst type :arrived flights')
                delayed=''  
                for flights in P1['data']:
                    if (flights['flight_status'=='delay']):
                        delayed+='Flight IATA code: ',flights['flight']['iataNumber']+'\n'               #Returns the IATA number of the flight.
                        delayed+='Departure airport name: ',flights['departure']['airport']+'\n'         #Returns the name of the departure airport.
                        delayed+='Original departure time: ',flights['departure']['scheduled']+'\n'      #Returns the scheduled departure date and time in RFC3339 (ISO8601) format.
                        delayed+='The estimated time of arrival: ',flights['arrival']['estimated']+'\n'  #Returns the estimated departure date and time in RFC3339 (ISO8601) format.
                        delayed+='Arrival terminal number: ',flights['arrival']['terminal']+'\n'         #Returns the arrival terminal.
                        delayed+='Delay time: ',flights['departure']['delay']+'\n'                       #Returns the departure delay in minutes.
                        delayed+='Arrival gate: ',flights['flight']['gate']+'\n'                         #Returns the arrival gate.
                print(delayed)
        
                
            
            
            
            elif request_num =='2':

              

              
               




        
        






#creating the socket and asssign IP and port number.
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_2:
    sock_2.bind(('127.0.0.1',1024))
    sock_2.listen()

    
#creating the thread.
t1=threading.Thread(name='thread 1')

#t1.start()

