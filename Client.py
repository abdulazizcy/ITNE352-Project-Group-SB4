import socket




#create a socket for client side 
socket_c= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Make a connection with the server by using connect methode 
socket_c.connect(("127.0.0.1",49999) )


