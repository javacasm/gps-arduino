#!/usr/bin/env python
# NMEA  sintax http://aprs.gids.nl/nmea/

$GPRMC - Recommended minimum specific GPS/Transit data
$GPRMC,152316.00,V,,,,,,,021015,,,N*78
$GPRMC,hhmmss.ss,A,llll.ll,a,yyyyy.yy,a,x.x,x.x,ddmmyy,x.x,

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