# gps-arduino

NMEA  sintax http://aprs.gids.nl/nmea/ (más info en http://www.gpsinformation.org/dale/nmea.htm)

Cadenas recogidas:

$GPRMC,152316.00,V,,,,,,,021015,,,N*78
$GPRMC - Recommended minimum specific GPS/Transit data
$GPRMC,hhmmss.ss,A,llll.ll,a,yyyyy.yy,a,x.x,x.x,ddmmyy,x.x,

$GPVTG,,,,,,,,,N*30
$GPVTG - Track made good and ground speed
$GPVTG,t,T,,,s.ss,N,s.ss,K*hh

$GPGGA,153227.00,,,,,0,04,23.02,,,,,,*61
$GPGGA - Global Positioning System Fix Data
GGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx

$GPGGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx*hh
		1			2	 3   4		5 6	 7
1    = UTC of Position
2    = Latitude
3    = N or S
4    = Longitude
5    = E or W
6    = GPS quality indicator (0=invalid; 1=GPS fix; 2=Diff. GPS fix)
7    = Number of satellites in use [not those in view]
8    = Horizontal dilution of position
9    = Antenna altitude above/below mean sea level (geoid)
10   = Meters  (Antenna height unit)
11   = Geoidal separation (Diff. between WGS-84 earth ellipsoid and
       mean sea level.  -=geoid is below WGS-84 ellipsoid)
12   = Meters  (Units of geoidal separation)
13   = Age in seconds since last update from diff. reference station
14   = Diff. reference station ID#
15   = Checksum

$GPGSA,A,1,32,11,04,01,,,,,,,,,42.06,23.02,35.20*33
$GPGSA - GPS DOP and active satellites

$GPGSV,4,1,13,01,68,053,23,03,74,308,13,04,45,092,12,08,22,161,09*75
$GPGSV,4,2,13,09,08,197,,11,64,114,27,14,02,032,,17,31,313,18*7A
$GPGSV,4,3,13,19,53,171,,23,41,173,18,28,19,261,18,31,05,078,*7B
$GPGSV,4,4,13,32,51,043,28*43
$GPGSV - GPS Satellites in view

$GPGLL,,,,,153227.00,V,N*4A
$GPGLL - Geographic position, latitude / longitude
$--GLL,lll.ll,a,yyyyy.yy,a,hhmmss.ss,A llll.ll = Latitude of position

$GPRMC,153228.00,V,,,,,,,021015,,,N*75
$GPVTG,,,,,,,,,N*30
$GPGGA,153228.00,,,,,0,03,11.20,,,,,,*68
$GPGSA,A,1,32,11,01,,,,,,,,,,11.25,11.20,1.00*04
$GPGSV,4,1,13,01,68,053,23,03,74,308,11,04,45,092,,08,22,161,10*7C
$GPGSV,4,2,13,09,08,197,,11,64,114,27,14,02,032,,17,31,313,18*7A
$GPGSV,4,3,13,19,53,171,,23,41,173,18,28,19,261,18,31,05,078,*7B
$GPGSV,4,4,13,32,51,043,28*43
$GPGLL,,,,,153228.00,V,N*45
$GPRMC,153229.00,V,,,,,,,021015,,,N*74
$GPVTG,,,,,,,,,N*30
$GPGGA,153229.00,,,,,0,03,11.21,,,,,,*68
$GPGSA,A,1,32,11,01,,,,,,,,,,11.25,11.21,1.00*05
$GPGSV,4,1,13,01,68,053,25,03,74,308,11,04,45,092,,08,22,161,11*7B
$GPGSV,4,2,13,09,08,197,,11,64,114,28,14,02,032,,17,31,313,17*7A
$GPGSV,4,3,13,19,53,171,,23,41,173,18,28,19,261,17,31,05,078,*74
$GPGSV,4,4,13,32,51,043,28*43
