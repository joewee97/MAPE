import datetime
from time import sleep
import RPi.GPIO as GPIO
import MySQLdb
import time

#photoresistor pinout GPIO20, pin 38
pin_to_circuit = 20
#lamp module pinout GPIO23, pin 16
lamp_pin = 23

#connect to MySQL database
con = MySQLdb.connect("localhost", user="joe", passwd = "capstone", db="plant")

#method to read values from photoresistor
def rc_time(pin_to_circuit):
    GPIO.setmode(GPIO.BCM)
    #hides warnings when executing script
    GPIO.setwarnings(False)
    count = 0
  
    #set output for GPIO to photoresistor first
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    while True:
        #prints current value of the photoresistor sensor
        print(rc_time(pin_to_circuit))
        value = rc_time(pin_to_circuit)
        #variable to hold based on condition and store in database
        lighting = ""
        #lower value represents brighter surroundings
        if(value<=30000):
            print("Lights are turned OFF!")
            #stores value as 1 for data visualisation purposes
            lighting = 0
            #sleep for 5 minutes
            time.sleep(1800)
        #skips condition when "if" condition is met,
        #since lamp turns on regardless of GPIO being HIGH or LOW
        else:
            print("Lights are turned ON!")
            #GPIO setup for lamp module within the else condition
            GPIO.setup(lamp_pin, GPIO.OUT)
            #GPIO.LOW turns on the lamp's relay module
            GPIO.output(lamp_pin, GPIO.LOW)
            #stores value as 1 for data visualisation purposes
            lighting = 1
            time.sleep(1800)
            #GPIO cleans up after 5 minutes
            #if not lamp module will remain on
            GPIO.cleanup()
        
        #MySQL data logging
        c = con.cursor()
        #runs the query
        c.execute("INSERT INTO light (lamp, led) VALUES (%s, %s)",[value, lighting])
        #sends query to the database
        con.commit()
        
        #method runs again after GPIO cleanup
        rc_time(pin_to_circuit)
        
#ends the script when user interrupts
except KeyboardInterrupt:
    pass
finally:
    #cleans up GPIO pin
    GPIO.cleanup()