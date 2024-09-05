import sys
from scapy.all import sniff

def pr_callback(pkt):
    print(pkt.show())

if __name__ == '__main__':

    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python3 network_sniffer.py <interface> [protocol] [number of packages]")
        print("Protocols available: icmp")
        sys.exit(1)

    interface = sys.argv[1]

    try:
        if len(sys.argv) == 2:
            sniff(iface=interface, prn=pr_callback)

        elif len(sys.argv) == 3:
            protocol = sys.argv[2]
            sniff(iface=interface, prn=pr_callback, filter=protocol)

        elif len(sys.argv) == 4:
            protocol = sys.argv[2]
            num_packets = int(sys.argv[3])
            sniff(iface=interface, prn=pr_callback, filter=protocol, count=num_packets)

    except KeyboardInterrupt:
        print("Keyboard Interrupt received, exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Exception: {str(e)}")
        sys.exit(1)
