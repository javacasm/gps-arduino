#!/usr/bin/env python
from time import sleep
import serial
ser = serial.Serial('/dev/ttyUSB1', 9600) # Establish the connection on a specific port
while True:
     print ser.readline() # Read the newest output from the Arduino
