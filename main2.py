#Second main method to run in a different terminal due to errors that affects the other scripts
#uses multiprocessing a well

import RPi.GPIO as GPIO
import time
import MySQLdb
from multiprocessing import Process

from pl import rc_time

#GPIO20, pin 38 for the photoresistor
pin_to_circuit = 20

def main():
    while True:
        p1 = Process(
            rc_time(pin_to_circuit)
            #time.sleep() runs through within pla1.py itself
            #30 minute idle within file pla.py
        )
        #multiprocessing engages
        p1.start()

if __name__ == "__main__":
    main()
