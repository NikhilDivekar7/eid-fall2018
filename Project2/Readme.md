This is the Repository for the EID project 2 - Websocket based Temperature and HUmidity Meter
By Anay Gondhalekar & Nikhil Divekar

Description: In this Project a websocket is created with server in python and client in HTML. Continuing with project 1, in this project, the temperature and humidity values obtained on the Qt are displayed every 5 secs and stored into a SQL data base. Then a server which creates a websocket to talk to the client sends the minimum, maximum and average values to the client on request of the client.

Run instructions:
1. First run the file finalworking.py to start getting the values on the Qt UI every 5 seconds and store them in the data base.
2. Then run the server.py file to create a socket for the server.
3. After creating the server open the RegFormAnay.html on the client side and enter the details as username:abcd and password as 12345678 and when the other html page opens enter the details of the connection like the port and the IP.

Extra Credit:
1. Graph is plotted of the humidity values.
2. Secure login
3. Reverse value rendering
4. Tab option to enhance UI
5. Print screen

Citation:
https://os.mbed.com/cookbook/Websockets-Server
Professor Bruce Montgomery's slides for EID 5053-002.
