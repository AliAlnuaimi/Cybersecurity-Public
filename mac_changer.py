# By: Ali Alnuaimi
#
#
# Purpose: Change the MAC Address of a particular
# Network interface
#
#

import subprocess

interface = input("Interface > ")
usrMAC = input("MAC Address > ")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", usrMAC])
subprocess.call(["ifconfig", interface, "up"])
