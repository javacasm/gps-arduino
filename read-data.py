#!/usr/bin/env python
# NMEA  sintax http://aprs.gids.nl/nmea/

from time import sleep
import serial
try:
	ser = serial.Serial('/dev/ttyUSB1', 9600) # Establish the connection on a specific port
	#ser.open()

	linea=''
	while True:
		try:
		   	serial_data = ser.read()
		   	if serial_data == '\n':
		   		print linea
		   		linea=''
		   	else:		
				linea=linea+serial_data
			
		except serial.serialutil.SerialException:
			#print "error"
			pass
except:
    pass    
finally:
    if ser:
        ser.close()