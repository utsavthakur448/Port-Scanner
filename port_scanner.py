import socket
import time
import threading
import argparse

startTime = time.time()

# Colors
CYAN = "\033[96m"
YELLOW  = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# ===== BANNER =====
print(YELLOW + r"""
 _   _ _______  __  _   _  ____   _____ ____    _    _   _ 
| \ | | ____\ \/ / | | | |/ ___| / ___/ ___|  / \  | \ | |
|  \| |  _|  \  /  | | | |\___ \| |   \___ \ / _ \ |  \| |
| |\  | |___ /  \  | |_| | ___) | |___ ___) / ___ \| |\  |
|_| \_|_____/_/\_\  \___/ |____/ \____|____/_/   \_\_| \_|

    *************************************************************************
    *|  NEXUSSCAN - Network Port Scanner                                    *
    *|  Developed By - Utsav Thakur                                         *
    *|  Features - TCP Port Scanning, Service Detection & Host Resolution   *
    *|  Email id - utsavthakur448@gmail.com                                 *
    *|  Linkedin Profile - www.linkedin.com/in/utsavthakur123               *
    *|  Github Profile - https://github.com/utsavthakur448                  * 
    *************************************************************************
        """ + RESET)

parser = argparse.ArgumentParser("Usage: port_scanner.py -t TARGET -sp [START_PORT] -ep [END_PORT]")
parser.add_argument("-t", "--target", required=True)
parser.add_argument("-sp", "--start-port")
parser.add_argument("-ep", "--end-port")
args = parser.parse_args()

target = args.target
start_port = int(args.start_port)
end_port = int(args.end_port)

# Resolve domain name to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(RED + "[-] Unable to resolve host." + RESET)
    exit()

print(CYAN + "[!] Starting scan on host: " + target + RESET)
print()
print("PORT    STATE        SERVICE")
print("-" * 60)

open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    conn = s.connect_ex((target_ip, port))
    if conn == 0:
        try:
            service = socket.getservbyport(port, "tcp")
            service = service.upper()
        except OSError:
            service = "UNKNOWN"
            
        open_ports.append(port)

        print("{:<8}{:<15}{}".format(port, "open", service) + RESET)
    s.close()

threads = []

for i in range(start_port, end_port + 1):
    thread = threading.Thread(target = scan_port, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
if len(open_ports) == 0:
    print(RED + "No open ports found.")
print()
print("Time elapsed: {:.2f} seconds".format(time.time() - startTime) + RESET)
