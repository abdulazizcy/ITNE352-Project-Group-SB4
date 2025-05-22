import socket
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_c.connect(("127.0.0.1", 49999))

name=input("Enter your User Name: ")
# Send the name to the server   
socket_c.send(name.encode("utf-8"))
while True:
    print("1 = Arrived flights")
    print("2 = Delayed flights")
    print("3 = Details of a particular flight")
    print("4 = Quit")
    #Take the request number from the user
    request=input("Enter Your Request Number: ")
    # Send the request number to the server
    socket_c.send(request.encode("utf-8"))
    
    if request == "1":
        response = socket_c.recv(4090).decode("utf-8")
        print(response)
        
    elif request == "2":
        response = socket_c.recv(4090).decode("utf-8")
        print(response)
        
    elif request == "3":
        flight_number = input("Enter the flight number: ")
        # Send the flight number to the server
        socket_c.send(flight_number.encode("utf-8"))
        response = socket_c.recv(4090).decode("utf-8")
        print(response)
        
    elif request == "4":
        socket_c.close()
        print("Connection closed")
        break
