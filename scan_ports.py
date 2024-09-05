from concurrent.futures import ThreadPoolExecutor
import socket
import sys

def scan_port(ip, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a TCP/IP socket.
        sock.settimeout(1) # Establish a maximum waiting time of 1 second.
        result = sock.connect_ex((ip, port)) # Tries to connect to the port.
        if result == 0:
            print(f"Port {port} is open.")
        sock.close()
    except KeyboardInterrupt:
        print("\nKeyboad Interrupt.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scan_ports.py <ip>")
        sys.exit()

    ip_to_scan = sys.argv[1]
    ports =range(1, 65535)

    print(f"Scanning host: {ip_to_scan}")

    with ThreadPoolExecutor() as executor: # Threading
        results = [executor.submit(scan_port, ip_to_scan, port) for port in ports]