import socket
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_c.connect(("127.0.0.1", 55555))

name=input("Enter your User Name: ")
# Send the name to the server   
socket_c.send(name.encode("ascii"))
while True:
    print("1 = Arrived flights")
    print("2 = Delayed flights")
    print("3 = Details of a particular flight")
    print("4 = Quit")
    #Take the request number from the user
    request=input("Enter Your Request Number: ")
    # Send the request number to the server
    socket_c.send(request.encode("ascii"))
    
    if request == "1":
        response = socket_c.recv(4090).decode("ascii")
        print(response)
        
    elif request == "2":
        response = socket_c.recv(4090).decode("ascii")
        print(response)
        
    elif request == "3":
        response = socket_c.recv(4090).decode("ascii")
        print(response)
        
    elif request == "4":
        socket_c.close()
        print("Connection closed")
        break
