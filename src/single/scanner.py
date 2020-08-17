#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import json

# Clear the screen
subprocess.call('clear', shell=True)

# Pull port range from config.json
with open("config.json") as json_file:
    data = json.load(json_file)
    loRange = int(data['range']['low'])
    hiRange = int(data['range']['high'])


# Ask for input
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print ("-" * 60)
print ("Please wait, scanning remote host....", remoteServerIP)
print ("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# scanning the port in range specified in config.json

try:
    for port in range(loRange,hiRange):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)
