#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import json
import os
import threading
import __builtin__
from multi.scanner_thread import split_processing

exc = getattr(__builtin__, "IOError", "FileNotFoundError")

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host....", remoteServerIP
print "-" * 60

# Resolves the relative path to absolute path
# [BUG]: https://github.com/vinitshahdeo/PortScanner/issues/19
def get_absolute_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    absolute_path = os.path.join(dir, *split_path)
    return absolute_path

# Check what time the scan started
t1 = datetime.now()

# Getting port range values from config.json
try:
    with open(get_absolute_path('../config.json')) as config_file:
        config = json.load(config_file)
        print get_absolute_path('../config.json')
    range_high = int(config['range']['high'])
    range_low = int(config['range']['low'])
    # defining number of threads running concurrently
    CONST_NUM_THREADS = int(config['thread']['count'])

except IOError:
    print("config.json file not found")
except ValueError:
    print("Kindly check the json file for appropriateness of range")

ports = list(range(range_low, range_high, 1))
# scanning the port only in range of (range_low, range_high)

def scan(ports, range_low, range_high):
    try:
        for port in range(range_low, range_high):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()


# calling function from scanner_thread.py for multithreading
split_processing(ports, CONST_NUM_THREADS, scan, range_low, range_high)

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
