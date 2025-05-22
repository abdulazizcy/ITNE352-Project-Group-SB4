# Multithreaded Flight arrival Client/Server Information System ITNE352-PROJECT-GROUP-SB4



# PROJECT DESCRPITION :

In our project we develops and create a client-server system that exchange information about flights at particular airport , The project coding topic include client-server architecture , network commuincation programming multithreading , API

------------------------------
# Semester:
**seecond Semester 2024-2025**  

# Group:
 - **group :**[SB4]
 - **Course code :** (ITNE352)
 - **section:**(2)
 - **Student name and ID:**
   
   1- ABDULAZIZ MOHD ABDULAZIZ / 20162158
   
   2- ALI HUSAIN MOOSA MOOSA /   20198285

-----------------





#  Table of contents
1-Requirements

2-How to run the system

3-The scripts

4-Acknowledgments

5-Conclusion

------------------------
# 1- Requirements 
- We need to download python into our local environment to run the system (( Essential))
----------------------------



# 2-How to run the system   
First of all, we need to open the terminal and make sure that in the right directory for the script,  run server script by typing (py server.py), then enter the airport code on another terminal run the client script by typing (py client.py). In this command, the client script will run, and it will print a message to enter the username of the client. Once the client enters the username, it will print several options to choose from (once the client enters one option of the list), and the server will respond based on that client option choice, and it will retrieve information from the API and send it to the client.

-------------------------------
# 3-The script 
In our project, there are two scripts, one for the server and the other for the client.

**server.py**

- The server script, once it starts, will ask the user to input an airport code.
- The server will use an API to retrieve 100 records of flights at a particular airport.
- Store the retrieved data into a JSON file called SB4.json.
- waits for client requests to connect to the server
- Accept the connection.
- store client name and display it
- Wait for the client to choose from the list of options, and once it makes a choice, reply with a proper response.

**client.py**

- Once the client script start it will create a tcp socket 
- the client script will connect to the server and will stay connected until the user or client choice quit option
- It will ask the user to input the username and send the username to the server throughout send() methode 
- the client script will show serveral option for user
- make the client to choice from that list of option and send request number to the server
- If the user selection request number is (1), the output will be on arrival flights (landed).
- If the user selection request number is (2), the output will be on delayed flights.
- If the user selection request number (3), the output will be on details of a particular flight, and the user will send the flight number with the request.
- If the user selction request to number (4) it will close the connection and quit 
- respond will show after choice made 

------------------------------------
# 4-Acknowledgments
We would like to thank our DR. Mohammed Almeer for his effort, knowledge, support, and guidance to make this project  success 

-----------------------------------


# 5-Conclusion

At the end of that project, we learned many things, such as Python programming, server-client system work, socket concept, how to use API to retrieve data and send it, and how to make multiple users connect at the same time using multi-threads. 
