import sys
import socket
from datetime import datetime



try: 
    
    target = input("Enter the host to scan: ")
    
    
except SyntaxError:
    print("Invalid host. Please enter a valid IP address or hostname.")
