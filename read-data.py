#!/usr/bin/env python
from time import sleep
import serial
try:
	ser = serial.Serial('/dev/ttyUSB1', 9600) # Establish the connection on a specific port
	#ser.open()

	while True:
		try:
		   	serial_data = ser.read()
			print serial_data
		except serial.serialutil.SerialException:
			#print "error"
			pass
except:
    pass    
finally:
    if ser:
        ser.close()