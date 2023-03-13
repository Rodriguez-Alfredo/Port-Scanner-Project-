#!/bin/python3

import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2: #amount of aguments allowed
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
	
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#add pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85): #loop scan from 50 thru 85
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #variable to gather ip address and port
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0: #0 means port is open 
			print(f"Port {port} is open")
		s.close() #if port is closed (1) and continues the loop

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit() #a safe exit of the program

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not connect to server.")
	sys.exit()

#Thank You TCM Security