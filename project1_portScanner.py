import sys
import socket
from datetime import datetime




    
target = sys.argv[1]
start_time = datetime.now()
print(f"Scan Started: {start_time}\nScanning target: {target}")
for port in range(1, 1035):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    results = sock.connect_ex((target, port))
    if results == 0:
        print(f"Port {port} is open")
        
        
    sock.close()
end_time = datetime.now()
total_time = end_time - start_time
print(f"Scan Completed: {end_time}")
print(f"Total Scan Time: {total_time}")
