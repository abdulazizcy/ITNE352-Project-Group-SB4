import socket
import requests 
import threading
import json



print('<<<<server has ben start>>>>')
airport_code=input('Enter the airport code :')



def connection (socka,address):
    client_name=socka.recv(2048).decode('utf-8') # to recive the clints name for clints side.
    print('THE CLIENT ',client_name,' IS CONNECTED.')

    #creating the parameters to pass thim to api.
    parameters= {
        'access_key': 'b5839f51c23a1a1f4cd15a24d5bd17bc' ,# api access key from the website acount.
        'arr_icao':airport_code,
        'limit':5  #the limit is by defult is 100.
    }
    # svaing the data recievd in file.
    with open ('group_SB4.json','w')as P1:
        # To get the response for the website with the parameters we set. 
        PP1=requests.get('https://api.aviationstack.com/v1/flights',parameters)
        
        json.dump(PP1.json(),P1,indent=3)
        
    while True:
        i=0
        request_num=socka.recv(4090).decode('utf-8') # to recive the requst form the clients.
        #to loade the data from the file.
        with open ('group_SB4.json','r') as P1:
            P2=json.load(P1)

            #creating if statment to chose the data that user want to see and save thime in new parameters.
            # to print the all arived flights.
            if request_num=="1":
                print('clinet name: ',client_name,'\n''requst type :arrived flights')
                fdata=''  
                for flights in P2['data']:
                    if (flights['flight_status']==['landed']):
                        fdata+='---------------------------------------------------------'+'\n'
                        fdata+='Flight IATA code: '+str(flights['flight']['iata'])+'\n'           #Returns the IATA number of the flight.
                        fdata+='Departure airport name: '+str(flights['departure']['airport'])+'\n'     #Returns the name of the departure airport.
                        fdata+='Arrival time: '+str(flights['arrival']['scheduled'])+'\n'                    #Returns the Arrival time.
                        fdata+='Arrival terminal number: '+str(flights['arrival']['terminal'])+'\n'     #Returns the arrival terminal.
                        fdata+='Arrival gate: '+str(flights['arrival']['gate'])+'\n'                     #Returns the arrival gate.
                        
                print(fdata)
                
            # to print the all delayed flights.
            elif request_num =='2':
                print('clinet name: ',client_name,'\n''requst type :delayed flights')
                fdata=''  
                for flights in P2['data']:
                    if (flights['departure']==['delay'])!= None:
                        fdata+='---------------------------------------------------------'+'\n'
                        fdata+='Flight IATA code: '+str(flights['flight']['iata'])+'\n'               #Returns the IATA number of the flight.
                        fdata+='Departure airport name: '+str(flights['departure']['airport'])+'\n'         #Returns the name of the departure airport.
                        fdata+='Original departure time: '+str(flights['departure']['scheduled'])+'\n'      #Returns the scheduled departure date and time in RFC3339 (ISO8601) format.
                        fdata+='The estimated time of arrival: '+str(flights['arrival']['estimated'])+'\n'  #Returns the estimated arrival date and time in RFC3339 (ISO8601) format.
                        fdata+='Arrival terminal number: '+str(flights['arrival']['terminal'])+'\n'         #Returns the arrival terminal.
                        fdata+='Delay time: '+str(flights['departure']['delay'])+'\n'                       #Returns the departure delay in minutes.
                        fdata+='Arrival gate: '+str(flights['arrival']['gate'])+'\n'                         #Returns the arrival gate.
                print(fdata)
            # to print Details of a particular flight.
            elif request_num =='3':
                print('clinet name: ',client_name,'\n''requst type :particular flights')
                particular_number=socka.recv(2011).decode('utf-8')
                fdata=''  
                for flights in P2['data']:
                    if particular_number==flights['flight']['number']:
                        fdata+='---------------------------------------------------------'+'\n'
                        fdata+='Flight IATA code: '+str(flights['flight']['iata'])+'\n'               #Returns the IATA number of the flight.
                        fdata+='Departure airport name: '+str(flights['departure']['airport'])+'\n'         #Returns the name of the departure airport.
                        fdata+='Departure airport gate: '+str(flights['departure']['gate'])+'\n'            #Returns the departure gate.
                        fdata+='Departure airport terminal: '+str(flights['departure']['terminal'])+'\n'    #Returns the departure terminal. 
                        fdata+='arrival airport name: '+str(flights['arrival']['airport'])+'\n'             #Returns the name of the arrival airport.
                        fdata+='arrival airport gate: '+str(flights['arrival']['gate'])+'\n'                #Returns the arrival gate.
                        fdata+='arrival airport terminal: '+str(flights['arrival']['terminal'])+'\n'        #Returns the arrival terminal.
                        fdata+='Flight status: '+str(flights['flight_status'])+'\n'                         #Returns the flight status. Possible values.
                        fdata+='scheduled departure time: '+str(flights['departure']['scheduled'])+'\n'     #Returns the scheduled departure date and time in RFC3339 (ISO8601) format.
                        fdata+='scheduled time of arrival: '+str(flights['arrival']['scheduled'])+'\n'      #Returns the scheduled arrival date and time in RFC3339 (ISO8601) format.       
                print(fdata)

            # to disconnect the server.
            elif request_num=='4':
                print ('<<<<server is disconnecting>>>>')
                #socka.colse()
                break
            socka.send(fdata.encode('utf-8'))
            
            

              


#creating the socket and asssign IP and port number.
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_2:
    sock_2.bind(('127.0.0.1',49999))
    sock_2.listen()
    # using while loop to accept muiltple connections from clinets.
    while True:
        socka,sockname=sock_2.accept()
        #creating the thread and start it.
        t1=threading.Thread(target=connection, args=(socka,sockname))
        t1.start()