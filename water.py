#Script for the water pump
import RPi.GPIO as GPIO
import time

#pin 11, GPIO17
moisture_pin = 17

#method used in method auto_w()
def moisture(moisture_pin=17):
    return GPIO.input(moisture_pin)

#GPIO04, pin 7 for pump module
#GPIO17, pin 11 for moisture sensor
def auto_w(pump_pin=4, moisture_pin=17):
    try:
        GPIO.setmode(GPIO.BCM)
        #hides warnings when executing script
        GPIO.setwarnings(False)
        #moisture sensor set as GPIO input
        GPIO.setup(moisture_pin, GPIO.IN)
        #water pump is set as GPIO output
        GPIO.setup(pump_pin, GPIO.OUT)
        #pump GPIO output set to off by default 
        GPIO.output(pump_pin, GPIO.LOW)
        isWet = moisture(moisture_pin) == 0
        #if output of isWet is False, the soil is dry
        print(isWet)
        
        #if soil is dry, water will be activated
        if not isWet:
            #GPIO.HIGH will trigger water pump 
            GPIO.output(pump_pin, GPIO.HIGH)
            time.sleep(2)
            #water pump is turned off
            GPIO.output(pump_pin, GPIO.LOW)
    
    #ends the script when user interrupts
    except KeyboardInterrupt:
        pass
    finally:
        #cleans up GPIO pin
        GPIO.cleanup()
        
