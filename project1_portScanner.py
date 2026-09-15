import sys
import socket
from datetime import datetime






target = sys.argv[1]
start_time = datetime.now()
services = {
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
        
    

print(f"[-] Scan Started: {start_time.strftime('%H:%M:%S')}\n[-] Scanning target: {target}\n")
print("[*] Scanning ports...\n",end="", flush=True)

for port in range(1, 1035):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    results = sock.connect_ex((target, port))
    if results == 0:
        service_name = services.get(port, "Unknown")
        print(f"\r[*]Port {port} ({service_name}): OPEN", flush=True)
        
        
    sock.close()
end_time = datetime.now()
total_time = end_time - start_time
print(f"\n[-] Scan Completed: {end_time.strftime('%H:%M:%S')}\n")
print(f"[-] Total Scan Time: {total_time}")

