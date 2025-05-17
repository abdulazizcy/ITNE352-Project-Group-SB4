import socket
#For gui we use tkinter built in library 
import tkinter as gui
#importing Themed Tkinter provides modern, native-looking widgets 
from tkinter import ttk



root = gui.Tk()
root.title("welcome ")
root.geometry("250x150")

ttk.Label(root, text="Enter Your UserName:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

button = ttk.Button(root, text="Send")
button.grid(row=1, column=0, columnspan=2, pady=5)


# Create a socket for client side
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make a connection with the server by using connect methode
socket_c.connect(("127.0.0.1", 49999))
#get user name from entry box 
name=name_entry.get()
# Send the name to the server
socket_c.send(name.encode("ascii"))
 



while True:
  
    root2 = gui.Tk()
    root2.title("enter your request number")
    root2.geometry("250x150")
    ttk.Label(root2, text="Request 1 = Arrived flights").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ttk.Label(root2, text="Request 2 = Delayed flights").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    ttk.Label(root2, text="Request 3 = Details of a particular flight:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    ttk.Label(root2, text=" Quit").grid(row=3, column=0, padx=5, pady=5, sticky="e")





    #Take the request number from the user
    ttk.Label(root2, text="Enter Your Request Number:").grid(row=4, column=0, padx=5, pady=5, sticky="e")

    request_entry = ttk.Entry(root2)
    request_entry.grid(row=4, column=1, padx=5, pady=5)
    # Get the request number from the entry box
    request=request_entry.get()
    # Send the request number to the server
    socket_c.send(request.encode("ascii"))
    # Create a label to display the response
    response_label = ttk.Label(root2, text="")
    response_label.grid(row=3, column=0, columnspan=2, pady=5)
    
    if request == "1":
        response = socket_c.recv(4090).decode("ascii")
        response_label.config(text=response)
        # Display the response in a message box
        gui.messagebox.showinfo("Response", response)

    elif request == "2":
        response = socket_c.recv(4090).decode("ascii")
        response_label.config(text=response)
         #Display the response in a message box
        gui.messagebox.showinfo("Response", response)

    elif request == "3":
        response = socket_c.recv(4090).decode("ascii")
        response_label.config(text=response)
        # Display the response in a message box
        gui.messagebox.showinfo("Response", response)

    elif request == "quit":
        socket_c.send(name + " Is quit from program ".encode("ascii"))
        # Close the socket and exit the program
        socket_c.close()
        break
        root2.mainloop()








root.mainloop()






