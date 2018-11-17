# Import needed modules from osc4py3
# https://osc4py3.readthedocs.io/en/latest/userdoc.html

from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm

def handlerfunction(s, x, y):
    # Will receive message data unpacked in s, x, y
    print('data')
    #print(s,x,y)
    pass

def handlerfunction2(address, s, x, y):
    # Will receive message address, and message data flattened in s, x, y
    pass

# Start the system.
osc_startup()
print('serving')
# Make server channels to receive packets.
#osc_udp_server("192.168.0.0", 3721, "aservername")
#osc_udp_server("0.0.0.0", 3724, "anotherserver")
#osc_udp_server("127.0.0.1", 12000, "aservername")
osc_udp_server("192.168.0.0", 12000, "aservername")

# Associate Python functions with message address patterns, using default
# argument scheme OSCARG_DATAUNPACK.
#osc_method("/wek/outputs/*", handlerfunction)
osc_method("/test/*", handlerfunction)
# Too, but request the message address pattern before in argscheme
#osc_method("/test/*", handlerfunction2, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)
print('serving2')
# Periodically call osc4py3 processing method in your event loop.
finished = False
while not finished:
    # …
    #print('s')
    osc_process()
    # …

# Properly close the system.
osc_terminate()