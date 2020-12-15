#main class to simultaneously run scripts using multiprocessing

import RPi.GPIO as GPIO
import time
from datetime import datetime
import MySQLdb
from multiprocessing import Process

from water import auto_w
from floater import floatStatus
from dht import dht11

pin_to_circuit = 20

def main():
    while True:
        p1 = Process(
            floatStatus()
        )
        
        p2 = Process(
            auto_w()
        )
        
        p3 = Process(
            dht11()
            )
        #This process is located in file main2.py
        #p4 = Process(
        #    rc_time(pin_to_circuit)
        #    )
        
        p1.start()
        p2.start()
        p3.start()
        #p4.start()
        
        
        time.sleep(1800)

if __name__ == "__main__":
    main()
