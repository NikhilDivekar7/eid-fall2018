Project 1: Local Qt-based Temperature and Humidity Measurement Unit
Author: Nikhil Divekar

The project is Temperature and Humidity measuremtn using Raspberry-Pi interfaced with DHT22 Sensor. The main requirements of the project were temperature and humidity should be displayed along with the time of request. It should also display some message if sensor is disconnected. The project also includes many additional features which are covered in Extra Credit topic.

Installation instruction:
1. Code should be cloned from Github on to the raspberry pi installed with raspbian
2. Interface the Raspberry Pi with DHT 22 Sensor with first two pins connected by 10K resistor. Analog value is read from GPIO pin 4.
3. Setup should be installed with Python3.
4. I have 3 UIs. Login window, Signup window and main window. Also there are 3 .py associated with each of them.
5. The program will start with the login window. Hence, in terminal we can start the program with Python3 login_main.py.
6. This opens up the login window which allows to enter credentials. If valid credentials are entered, user is redirected to the main   screen. Also, there is option for signup which will take you to signup window where you can create the new account. Entering wrong info in login window will result into warning message box.
7. In the main, window you can see the immediate value of temperature and humidity on the button press. You can also get values every 3 seconds by enabling auto-refresh. Average value of temp and humidity is also displayed. The plot of temperature and humidity can also be displayed on the button press. User can shit from celsius to fahrenheit and vice a versa. This system gives out warning in case of disconnected sensor or temperature or humidity out of range.
8. Users can also modify the limits of minimum and maximum temperature or humidity.

Extra Credit( Project Additional features):
1. Secure login system with database connected, with features of creating new account as well as logging into an existing account.
2. User can display temperature in celsius or Fahrenheit format.
3. Temperature and Humidity graphs can be plotted.
4. Values of temperature and humidity can be auto-refreshed every 3 seconds.
5. Users can specify the range for temperature and humidity.

References:
1. https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/
2. https://www.youtube.com/watch?v=4Y5zjTJ9LV4
3. https://stackoverflow.com/questions/44011259/embedding-a-graph-into-a-gui-qtdesigner-and-pyside
4. https://pythonspot.com/pyqt5/

