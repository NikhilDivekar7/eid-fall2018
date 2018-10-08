This is the .js file for Homework 2 of Embeded Interface Design
This code outputs temperature and humidity readings recorded by DHT22 Sensor every 10 seconds
It also records lowest, highest and average of 10 temperature and humidity readings
Author	: Nikhil Divekar
File-name 	: dht22.js
node version : v8.12.0

Build steps:
1. First install nodejs on raspberry pi.
2. For that you have to download the compatible version of nodejs and extract that. (https://nodejs.org/en/download/)
3. Change directory into extracted folder and then run (sudo cp -R * /usr/local/)
4. Next, install BCN2835 libraries (http://www.airspayce.com/mikem/bcm2835/bcm2835-1.57.tar.gz)
5. Setup those libraries and then we can install dht22 libraries with (npm install rpi-dht-sensor)
6. Next write the code and run with node <file_name> command.

References:
1. https://www.npmjs.com/package/rpi-dht-sensor
2. https://www.instructables.com/id/Install-Nodejs-and-Npm-on-Raspberry-Pi/
3. http://book.mixu.net/node/ch5.html
