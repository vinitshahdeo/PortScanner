#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import json
import threading
import __builtin__

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

# Check what time the scan started
t1 = datetime.now()

# Getting port range values from config.json
try:
    with open('config.json') as config_file:
        config = json.load(config_file)
    range_high = int(config['range']['high'])
    range_low = int(config['range']['low'])

except IOError:
    print("config.json file not found")
except ValueError:
    print("Kindly check the json file for appropriateness of range")

ports = list(range(range_low, range_high, 1))
# scanning the port only in range of (1, 8888)


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


# defining number of threads running concurrently
CONST_NUM_THREADS = 8


def split_processing(ports, num_splits=CONST_NUM_THREADS):
    split_size = (range_high-range_low) // num_splits
    threads = []
    for i in range(num_splits):
        # determine the indices of the list this thread will handle
        start = i * split_size
        # special case on the last chunk to account for uneven splits
        end = range_high if i+1 == num_splits else (i+1) * split_size
        # create the thread
        threads.append(
            threading.Thread(target=scan, args=(ports, start, end)))
        threads[-1].start()  # start the thread we just created

    # wait for all threads to finish
    for t in threads:
        t.join()


split_processing(ports)

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
