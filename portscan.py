# Author: Ali Alnuaimi
#
# Purpose: basic port scanner, will check open ports
# given a host name and a port range, as well as
# producing a report afterwards
#
# For education purposes only

import os
import sys
import socket
import threading
from datetime import datetime
from queue import Queue


host = '192.168.0.168' #The IP Address or HostName of the target
min_port = 1 #Min Port in the range
max_port = 25 #Max Port in the range
report = True #Create a Report after done

print_lock = threading.Lock()
open_ports = []

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host, port))
        with print_lock:
            open_ports.append(port)
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

#Append scan results in a .txt file
def report():
    file_name = "port_scan_report.txt"
    f = open(file_name, "a+")
    scan_range_str = "(Range: " + str(min_port) + "~" + str(max_port) + ")"
    datetime_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f.write("\nNew portscan " + scan_range_str + " for host "
            + host + " at " + datetime_str + ":")
    f.write("\n")
    if len(open_ports) <= 0:
        f.write("\n\tAll ports in specified range are closed")
    else:
        for x in open_ports:
            f.write("\n\tPort " + str(x) + " Is Open")
    f.write("\n")
    f.close()
    os.system('cmd /c "start "' + file_name)

q = Queue()

#How many Threads to run at a time
for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

#Port Range to Scan For
for worker in range(min_port, max_port+1):
    q.put(worker)
    q.join()

if (report):
    report()
