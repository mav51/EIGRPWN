# EIGRPWN

**The author has nothing to do with those who will use this tool for personal purposes to destroy other people's computer networks. The tools are presented for training purposes to help engineers improve the security of their network.**

**routeinject.py** - tool for route injection in the EIGRP domain.

**helloflooding.py** - tool for exploitation a DoS attack, flooding with EIGRP "Hello" messages. When flooding "Hello" messages, fake EIGRP neighbors are generate

**routingtableoverflow.py** - this script causes an overflow of the routing table of the EIGRP router by generating fake routes at high speed.

```
python3 routeinject.py --help

███████╗██╗░██████╗░██████╗░██████╗░░██╗░░░░░░░██╗███╗░░██╗
██╔════╝██║██╔════╝░██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
█████╗░░██║██║░░██╗░██████╔╝██████╔╝░╚██╗████╗██╔╝██╔██╗██║
██╔══╝░░██║██║░░╚██╗██╔══██╗██╔═══╝░░░████╔═████║░██║╚████║
███████╗██║╚██████╔╝██║░░██║██║░░░░░░░╚██╔╝░╚██╔╝░██║░╚███║
╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
    
EIGRP route injection tool

Author: @necreas1ng, <necreas1ng@protonmail.com>

usage: routeinject.py [-h] --interface INTERFACE --asn ASN --src SOURCE_IP --dst DESTINATION_IP --prefix PREFIX

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Choose the interface to attack
  --asn ASN             Specify the EIGRP AS Number
  --src SOURCE_IP       Specify your IP Address
  --dst DESTINATION_IP  Target IP address for injection
  --prefix PREFIX       Specifying the subnet mask
  
  ```
  
  ```
  python3 helloflooding.py --help
  
███████╗██╗░██████╗░██████╗░██████╗░░██╗░░░░░░░██╗███╗░░██╗
██╔════╝██║██╔════╝░██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
█████╗░░██║██║░░██╗░██████╔╝██████╔╝░╚██╗████╗██╔╝██╔██╗██║
██╔══╝░░██║██║░░╚██╗██╔══██╗██╔═══╝░░░████╔═████║░██║╚████║
███████╗██║╚██████╔╝██║░░██║██║░░░░░░░╚██╔╝░╚██╔╝░██║░╚███║
╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
    
EIGRP Hello flooding tool (Denial of Service)

Author: @necreas1ng, <necreas1ng@protonmail.com>

usage: helloflooding.py [-h] --interface INTERFACE --asn ASN --subnet SUBNET

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Choose the interface to attack
  --asn ASN             Specify the EIGRP AS Number
  --subnet SUBNET       Specify the subnet. Example: 10.10.10.0/24
  
  
  ```
  python3 routingtableoverflow.py --help
  
███████╗██╗░██████╗░██████╗░██████╗░░██╗░░░░░░░██╗███╗░░██╗
██╔════╝██║██╔════╝░██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
█████╗░░██║██║░░██╗░██████╔╝██████╔╝░╚██╗████╗██╔╝██╔██╗██║
██╔══╝░░██║██║░░╚██╗██╔══██╗██╔═══╝░░░████╔═████║░██║╚████║
███████╗██║╚██████╔╝██║░░██║██║░░░░░░░╚██╔╝░╚██╔╝░██║░╚███║
╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
    
Tool for overflow of routing tables in EIGRP routers

Author: @necreas1ng, <necreas1ng@protonmail.com>

usage: routingtableoverflow.py [-h] --interface INTERFACE --asn ASN --src SOURCE_IP

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Choose the interface to attack
  --asn ASN             Specify the EIGRP AS Number
  --src SOURCE_IP       Specify your IP Address
  
  ```

