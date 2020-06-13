import socket
from datetime import datetime
import json
import os
from multi.scanner_thread import split_processing

# Ask for input
net1 = raw_input('Enter the IP address: ')
net2 = net1.split('.')
a = '.'
net3 = net2[0] + a + net2[1] + a + net2[2] + a

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning IP address....", net3+"XXX"
print "-" * 60

# Resolves the relative path to absolute path
# [BUG]: https://github.com/vinitshahdeo/PortScanner/issues/19


def get_absolute_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    absolute_path = os.path.join(dir, *split_path)
    return absolute_path


# Check what time the scan started
td1 = datetime.now()

try:
    with open(get_absolute_path('../config.json')) as config_file:
        config = json.load(config_file)
        # print get_absolute_path('../config.json')
    range_low = int(config['ipRange']['low'])
    range_high = int(config['ipRange']['high'])
    # defining number of threads running concurrently
    CONST_NUM_THREADS = int(config['thread']['count'])

except IOError:
    print("config.json file not found")
except ValueError:
    print("Kindly check the json file for appropriateness of range")

ips = list(range(range_low, range_high, 1))
# scanning the port only in range of (range_low, range_high)
range_high = range_high + 1
# including the last address at 'range_high'


def scan(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr, 135))
    # 'result' is used as error indicator, port 135 is used for Windows
    # 137, 138, 139, 445 can also be used
    if result == 0:
        # tests if IP address is live
        return 1
    else:
        return 0


def run1(ips, range_low, range_high):
    for ip in xrange(range_low, range_high):
        addr = net3+str(ip)
        # gets full address
        if (scan(addr)):
            print addr + " is live\n"


# calling function from scanner_thread.py for multithreading
split_processing(ips, CONST_NUM_THREADS, run1, range_low, range_high)
# Checking the time again
td2 = datetime.now()
# Calculates the difference of time, to see how long it took to run the script
total = td2-td1
# Printing the information to screen
print "Scanning completed in ", total
