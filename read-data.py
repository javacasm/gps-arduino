#!/usr/bin/env python
# NMEA  sintax http://aprs.gids.nl/nmea/

from time import sleep
import serial
import re

# Calculate checksums 
# http://doschman.blogspot.com.es/2013/01/calculating-nmea-sentence-checksums.html

def chksum_nmea(sentence):
	
    # This is a string, will need to convert it to hex for 
    # proper comparsion below

    cksum = sentence[len(sentence) - 2:]
    
    # String slicing: Grabs all the characters 
    # between '$' and '*' and nukes any lingering
    # newline or CRLF

    chksumdata = re.sub("(\n|\r\n)","", sentence[sentence.find("$")+1:sentence.find("*")])

    # Initializing our first XOR value
    csum = 0 
    
    # For each char in chksumdata, XOR against the previous 
    # XOR'd char.  The final XOR of the last char will be our 
    # checksum to verify against the checksum we sliced off 
    # the NMEA sentence
    
    for c in chksumdata:
       # XOR'ing value of csum against the next char in line
       # and storing the new XOR value in csum
       csum ^= ord(c)
    
    # Do we have a validated sentence?
    if hex(csum) == hex(int(cksum, 16)):
       return True

    return False

ser = None
try:
	ser = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port
	#ser.open()

	linea=''
	while True:
		try:
		   	serial_data = ser.read()
		   	if serial_data == '\r' :
		   		checksum = chksum_nmea(linea)
		   		mensaje=None
		   		if checksum:
		   		# http://raspberrypi.stackexchange.com/questions/12029/extracting-required-information-from-nmea-gps-data
				# Extract the data from GPGGA sentence
					lat=None
					lon=None
					IsGPGGA=linea.startswith( '$GPGGA' )
					if IsGPGGA:
						lat, _, lon = linea.strip().split(',')[2:5]		   			
						mensaje = ">>> ("+ lat+" , "+lon+") "+  linea
					else:	
						mensaje = "OK "+ linea
		   		else:
		   			mensaje = "ERROR "+ linea
		   		print mensaje
		   		linea=''
		   	else:		
		   		if serial_data != '\n':
					linea=linea+serial_data
			
		except serial.serialutil.SerialException:
			#print "error"
			pass
except Exception as e:
	print e
finally:
    if ser:
        ser.close()

