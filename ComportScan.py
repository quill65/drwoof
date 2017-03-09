#!/usr/bin/env python

import serial, glob, platform
from serial.tools import list_ports

# A function that tries to list serial ports on most common platforms
def list_all_serial_ports():

##    print "list_all_serial_ports:"
    
    system_name = platform.system()
    if system_name == "Windows":
        # Scan for available ports.
        ports = list_ports.comports()
        available = []
        for port in ports:
##            print "adding port %s - %s" % (port[0], port[1])
            available.append(port[0])
        
##        available = []
##        for i in range(256):
##            try:
##                s = serial.Serial(i)
##                available.append("COM"+str(i+1))
##                s.close()
##                print "trying port %d: %s" % (i, "COM"+str(i+1))
##                
##            except serial.SerialException:
##                print "trying port %d: nothing" % (i)
##                pass
##        print "DONE list all serial ports:"
        return available
    elif system_name == "Darwin":
        # Mac
        return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
    else:
        # Assume Linux or something else
        return  glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyS*')
        
# A function that tries to list available (openable) serial ports on most common platforms
def list_available_serial_ports():
    
    availableports = []
    
    allports = list_all_serial_ports()

##    print "list available serial ports:"
    for portname in allports:
        try:
            ser = serial.Serial(portname, baudrate=9600, timeout=0)
            ser.close()
            availableports.append(portname)
##            print "trying port %s = ok" % (portname)
        except:
##            print "trying port %s = fail" % (portname)
            pass
                
##    print "DONE list_available_serial_ports"
    return availableports
    


