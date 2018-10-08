// This is the .js file for Homework 2 of Embeded Interface Design
// This code outputs temperature and humidity readings recorded by DHT22 Sensor every 10 seconds
// It also records lowest, highest and average of 10 temperature and humidity readings
// Author	: Nikhil Divekar
// File-name 	: dht22.js
// node version : v8.12.0


var rpiDHTSensor = require('rpi-dht-sensor');						// use rpi-dht-sensor libraries present in bcm2835 folder
 
var temp_hum_sensor = new rpiDHTSensor.DHT22(4);					// get the values from GPIO 4 pin
var final_count = 10

var count = 0;
var temparray = new Array();
var temp_sum = 0;
var avg_temp = 0;
var tempF;

var humarray = new Array();
var hum_sum = 0;
var avg_hum = 0;
 
function read ()
{
  var readout = temp_hum_sensor.read();							// read sensor value

  tempF = ((9 * readout.temperature.toFixed(2))/5) + 32;				// convert temperature to Fahrenheit
  tempF = tempF.toFixed(2);							
  console.log((count+1) + '.' +'Temperature: ' + tempF + ' degF, ' +
        'humidity: ' + readout.humidity.toFixed(2) + '% Hum');				// log the readings

  temparray.push(tempF);							
  humarray.push(readout.humidity.toFixed(2));						// push the readings on to the array

  if(count == final_count-1)								// check for the readings count
  {
	console.log()
	console.log('Lowest temperature: ' + Math.min(...temparray).toFixed(2));	// lowest temperature
	console.log('Highest temperature: ' + Math.max(...temparray).toFixed(2));	// highest temperature
	for(var i = 0; i < temparray.length; i++)
	{
		temp_sum += parseFloat(temparray[i]);
	}
	avg_temp = parseFloat(temp_sum/temparray.length);
	avg_temp = avg_temp.toFixed(2);
	console.log('Average temperature: ' + avg_temp);				// average temperature 
	temparray = [];

	console.log()
	console.log('Lowest humidity: ' + Math.min(...humarray).toFixed(2));		// lowest humidity
	console.log('Highest humidity: ' + Math.max(...humarray).toFixed(2));		// highest humidity
	for(var i = 0; i < humarray.length; i++)
	{
		hum_sum += parseFloat(humarray[i]);
	}
	avg_hum = parseFloat(hum_sum/humarray.length);
	avg_hum = avg_hum.toFixed(2);
	console.log('Average humidity: ' + avg_hum);					// average humidity
	humarray = [];
  }
  count++;
  if(count < final_count)
  {
	setTimeout(read, 10000);							// recursive call
  }  
}

read();											// first time function called
