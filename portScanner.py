
import sys   # This module allows the program to accept command line arguments
import socket   # This module is used to communicate with the target over the network
from datetime import datetime # This module is used to measure the time the scan takes to complete




if len(sys.argv) < 2:#This line checks if the user has provided a target IP address as a command line argument
    print("\n[~] Error: No target IP address provided.\n") #displays an error message
    sys.exit(1) #This line stops the program with an error message 

target = sys.argv[1] # This variable stores the target IP address that was provided on the command line
start_time = datetime.now() # This variable stores the time when the scan began

services = { # This dictionary stores the common ports and their service names
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3389: "RDP"
}

try:
    print(f"\n[-] Scan Started: {start_time.strftime('%H:%M:%S')}\n[-] Scanning target: {target}")
    # This line prints the time that the scan began and the target IP address

    print("[-] Scanning range: 1-1034\n")
    # This line displays the range of ports that are to be scanned

    print("[*] Scanning ports...",end="", flush=True)
    # This line prints a message that says that the ports are being scanned
    # The end="" argument is used to prevent the print function from adding a new line after the message
    # The flush=True argument is used to force the output to be printed as soon as possible
    numOfPorts=0


    for port in range(1, 1035): # This loop iterates through the range of ports from 1 to 1034
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This line creates a new socket object using the AF_INET address family and SOCK_STREAM socket type
        # AF_INET is used for IPv4 addresses
        # SOCK_STREAM is used for establishing TCP connections

        sock.settimeout(0.5)
        # This line is used to set a timeout for the socket connection with the purpose of preventing the program from waiting indefinitely
        
        
        results = sock.connect_ex((target, port))
        # This line attempts to connect to the target IP address and port number by using the connect_ex() method
        # If the connection is successful, the method returns 0, indicating that the port is open

        if results == 0:
            # This line checks the result of the connection attempt to see if it returned a 0
            numOfPorts=numOfPorts+1
            # This will make it so that if a port if sound open then will add one for every port that is found
            service_name = services.get(port, "Unknown")
            # This line is used when the port is open but its service is not found in the services dictionary

            print(f"\r[*] Port {port} ({service_name}): OPEN{" " * 20}", flush=True)
            # This line prints the port number of the opened port and its service name if the service name is found in the services dictionary
            # The flush=True argument is used to force the output to be printed immediately
            print("[*] Scanning ports...",end="", flush=True)
            
        


        sock.close()
        # This line closes the socket connection
    print("\r"+" " * 60+"\r",end="",flush=True)
    # this lines Removes the Scanning Port.. message and the end by pelacing it with 60 spaces
        
except socket.gaierror:
    #This line is used when a gaierror is found and displayes the message below 
    print("\n[~] Error: Invalid IP address.\n", flush=True)
    #This line displays the Error message
    sys.exit(1)
    #This line stops the program with an error message 

if numOfPorts ==0:
    print(f"[*] No open ports detected{" " * 20}",flush=True)
    #This IF statmetns makes it so that if no port is found then the variable numOfPorts will stay 0 and therefore display this message


end_time = datetime.now()
# This line collects the time the scan finished and stores it

total_time = end_time - start_time
# This line calculates the total time taken for the scan
print(f"\n[-] Number of open ports: {numOfPorts}")
# Displays the total number of open ports
print(f"[-] Scan Completed: {end_time.strftime('%H:%M:%S')}")
# This line displays the time the scan finished
print(f"[-] Total Scan Time: {total_time}\n")
# This line displays the total time taken to complete the scan

