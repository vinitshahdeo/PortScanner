import socket
import sys
import argparse
from datetime import datetime
import json
import os
from multi.scanner_thread import split_processing

#===================================================================================================
# Get the input through flag. If the not used get input from the file and the user.
"""
Way to use flag:
    python3 ipscanner.py -r <range> -t <number_of_thread> -i <ip_address> 
For example:
    python3 ipscanner.py -r 0-255 -t 8 -i 194.165.43.2
    Here, the range is from 0 to 255, number of thread is 8 and the ip address is 194.165.43.2
"""
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', "--range", dest="range", help="To specify the range of ip like 0-255 (This flag is optional.If not mensioned, the range will taken from the config.json file)")
    parser.add_argument("-t", "--thread", dest="thread", help="To specify the number of threading to be used like 8 (This flag is optional.If not mensioned, the thread number will taken from the config.json file)")
    parser.add_argument('-i', "--ip", dest="ip", help="To specify the ip address to scan, like 194.165.43.2 (This flag is optional. If not mensioned script ask for input)")
    argument = parser.parse_args()
    #If the range flag is used, it process the range.
    if argument.range:
        range = argument.range.split('-')
        range_low = int(range[0])
        range_high = int(range[1])
    #If thread flag is used, assign it to CONST_NUM_THREADS
    if argument.thread:
        CONST_NUM_THREADS = int(argument.thread)
    #If ip flag is used, assign it to net1 else get from user
    if argument.ip:
        net1 = argument.ip
    else:
        net1 = input('Enter the IP address: ')
    net2 = net1.split('.')
    a = '.'
    net3 = net2[0] + a + net2[1] + a + net2[2] + a

    # The config.json file is accessed only when the range or thread not get from the user.
    if not(argument.range and argument.thread):
        try:
            with open(get_absolute_path('../config.json')) as config_file:
                config = json.load(config_file)
                # print get_absolute_path('../config.json')
            if not argument.range:
                range_low = int(config['ipRange']['low'])
                range_high = int(config['ipRange']['high'])
            if not argument.thread:
                # defining number of threads running concurrently
                CONST_NUM_THREADS = int(config['thread']['count'])

        except IOError:
            print("config.json file not found")
            sys.exit()
        except ValueError:
            print("Kindly check the json file for appropriateness of range")
            sys.exit()
    return range_low, range_high, CONST_NUM_THREADS, net3

#===============================================================================================

# Resolves the relative path to absolute path
# [BUG]: https://github.com/vinitshahdeo/PortScanner/issues/19


def get_absolute_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    absolute_path = os.path.join(dir, *split_path)
    return absolute_path

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
    for ip in range(range_low, range_high):
        addr = net3+str(ip)
        # gets full address
        if (scan(addr)):
            print(addr + " is live\n")

# Get input
range_low, range_high, CONST_NUM_THREADS, net3 = get_arguments()

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning IP address....", net3+"XXX")
print("-" * 60)



# Check what time the scan started
td1 = datetime.now()



ips = list(range(range_low, range_high, 1))
# scanning the port only in range of (range_low, range_high)
range_high = range_high + 1
# including the last address at 'range_high'




# calling function from scanner_thread.py for multithreading
split_processing(ips, CONST_NUM_THREADS, run1, range_low, range_high)
# Checking the time again
td2 = datetime.now()
# Calculates the difference of time, to see how long it took to run the script
total = td2-td1
# Printing the information to screen
print("Scanning completed in ", total)