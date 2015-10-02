#!/usr/bin/env python
# NMEA  sintax http://aprs.gids.nl/nmea/

from time import sleep
import serial

# Calculate checksums 
# http://doschman.blogspot.com.es/2013/01/calculating-nmea-sentence-checksums.html

def chksum_nmea(sentence):
	
    # This is a string, will need to convert it to hex for 
    # proper comparsion below
    print sentence
    

    cksum = sentence[len(sentence) - 2:]
    
    # String slicing: Grabs all the characters 
    # between '$' and '*' and nukes any lingering
    # newline or CRLF

    print cksum

    chksumdata = re.sub("(\n|\r\n)","", sentence[sentence.find("$")+1:sentence.find("*")])
    print chksumdata    
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
		   		if checksum:
		   			linea="OK "+ linea
		   		else:
		   			linea="ERROR "+ linea
		   		print linea
		   		linea=''
		   	else:		
		   		if serial_data != '\n':
					linea=linea+serial_data
			
		except serial.serialutil.SerialException:
			#print "error"
			pass
except Exception as e:
	print e.Message
finally:
    if ser:
        ser.close()

