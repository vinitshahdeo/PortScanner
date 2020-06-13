import socket
from datetime import datetime
import json
import os


net1 = raw_input('Enter the IP address: ')
net2 = net1.split('.')
a = '.'
net3 = net2[0] + a + net2[1] + a + net2[2] + a


def get_absolute_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    absolute_path = os.path.join(dir, *split_path)
    return absolute_path


try:
    with open(get_absolute_path('../config.json')) as config_file:
        config = json.load(config_file)
        print get_absolute_path('../config.json')
    stn1 = int(config['iprange']['low'])
    edn1 = int(config['iprange']['high'])
    # defining number of threads running concurrently
    CONST_NUM_THREADS = int(config['thread']['count'])

except IOError:
    print("config.json file not found")
except ValueError:
    print("Kindly check the json file for appropriateness of range")

edn1 = edn1 + 1
td1 = datetime.now()

def scan(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr, 135))
    if result == 0:
        return 1
    else:
        return 0


def run1():
    for ip in xrange(stn1, edn1):
        addr = net3+str(ip)
        if (scan(addr)):
            print addr, "this address is live"


run1()

td2 = datetime.now()
total = td2-td1
print "scanning complete in ", total
