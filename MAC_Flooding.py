import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

L2=Ether()
L2.src=RandMAC()
L2.dst="FF:FF:FF:FF:FF:FF"

L2
<Ether dst=FF:FF:FF:FF:FF:FF src=3e:b0:61:40:97:4d |>
 

L2
<Ether dst=FF:FF:FF:FF:FF:FF src=5c:1e:04:41:8c:d0 |>
                                        

L2
<Ether dst=FF:FF:FF:FF:FF:FF src=91:ea:c8:4d:67:9c |>

sendp(L2,loop=1)
