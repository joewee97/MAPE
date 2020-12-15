# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:26:17 2020

@author: Joe
"""
#DHT11 sensor script to detect temperature and humidity
import time
from datetime import datetime
import Adafruit_DHT
import MySQLdb
import RPi.GPIO as GPIO

#connect to MySQL database
con = MySQLdb.connect("localhost", user="joe", passwd = "capstone", db="plant")

#variable to store Adafruit sensor functions
DHT_SENSOR = Adafruit_DHT.DHT11
#GPIO 4, pin 7 / GPIO 10, pin 19
DHT_PIN = 10

#method to run dht11 sensor functions
def dht11():
    try:        
        #variables used to store corresponding values
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if temperature is not None and humidity is not None:
            print("Temperature={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
            
            #MySQL data logging
            c = con.cursor()
            #runs the query
            c.execute("INSERT INTO temphumid (temp, humid) VALUES (%s, %s)",
            (temperature, humidity))
            #sends query to the database
            con.commit()
        else:
            #sensor failure
            print("Sensor failure. Check for errors!")
    #ends the script when user interrupts
    except KeyboardInterrupt:
        pass
    finally:
        #cleans up GPIO pin
        GPIO.cleanup()
        
