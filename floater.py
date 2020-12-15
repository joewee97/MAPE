import RPi.GPIO as GPIO
import time
import MySQLdb
from mail import sendUserMail


#GPIO07, 26 for floater switch

def floatStatus():
    GPIO.setmode(GPIO.BCM)
    #hides warnings when executing script
    GPIO.setwarnings(False)
    GPIO.setup(7,GPIO.IN, GPIO.PUD_UP)
    #variable to store integer
    saveFloat = ""
    float_pin = GPIO.input(7)
    if float_pin == False:
        print('Button pressed')
        print(float_pin)
        #stores value 0 for data visualization purposes
        saveFloat = 0
        currentStatus = "Depleted"
        print(saveFloat)
        #if depleted, send email via smtp
        sendUserMail()
        
    else:
        print('Button unpressed')
        print(float_pin)
        #saveFloat = "Present"
        #stores value 1 for data visualization purposes
        saveFloat = 1
        currentStatus = "Present"
        print(saveFloat)
    
    try:
        #connect to MySQL database
        con = MySQLdb.connect(host="localhost", user="joe", passwd = "capstone", db="plant")
        #MySQL data logging
        c = con.cursor()
        #runs the query
        c.execute("INSERT INTO tfloat (storage) VALUES (%s)",[saveFloat])
        #sends query to the database
        con.commit()

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
