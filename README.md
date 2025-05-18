# Multithreaded Flight arrival Client/Server Information System ITNE352-PROJECT-GROUP-SB4



# PROJECT DESCRPITION :

In our project we develops and create a client-server system that exchange information about flights at particular airport , The project coding topic include client-server architecture , network commuincation programming multithreading , API

# Semester:
**seecond Semester 2024-2025**  

# Group:
 - **group :**[SB4]
 - **Course code :** (ITNE352)
 - **section:**(2)
 - **Student name and ID:**
   
   1- ABDULAZIZ MOHD ABDULAZIZ / 20162158
   
   2- ALI HUSAIN MOOSA MOOSA /   20198285

#  Table of contents
1-Requirements

2-How to run the system

3-The scripts

4-Acknowledgments

5-Conclusion

# 1- Requirements 
- We need to download python into our local environment to run the system (( Essential))



# 2-How to run the system   
First of all we need to open the terminal and make srue that in the right directory as the script it run server script by typing (py server.py) then enter the airport code on another terminal run the client script by typing ( py client.py) in this command the client script will run and it will print message to enter the user nmae of client once entered user name it will print several options to choices from (once the client enter one option of the list ) the server will respond base on that client option choice and it will retrive information from api and send to the client .


# 3-The script 
In our project there are two script one for server and the other one for client 


**server.py**

- The server script once it start it will ask the user to input airport code
- The server will using API to retrieve 100 record of flights at particular airport
- store the retrieved data into a jason file called SB4.jason
- waits for client request to connect to the server
- accept the connection
- store client name and display it
- wait for client to choice from list of option and once it made a choice reply with proper respond 

**client.py**
- the client script will connect to the server and will stay connected until the user or client choice quit option
- the client script will show serveral option for user
- make the client to choice from that list of option
- respond will show after choice made 


# 4-Acknowledgments
we would like to thanks our DR.Mohammed Almeer for his effort , knowlege, support , guidance to make this project  success 




# 5-Conclusion
At the end of that project we learned many things such as python programming , server-clientn system work , socket concept , how to use api to retrieve data and send it , how to make multiable users connect at the same time using multi-threads . 
