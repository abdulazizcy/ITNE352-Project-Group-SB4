import socket
#for gui we use tkinter built in library 
import tkinter as gui
# importing Themed Tkinter provides modern, native-looking widgets 
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
 
root.mainloop()