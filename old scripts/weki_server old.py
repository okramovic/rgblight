#  https://pypi.org/project/python-osc/
import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()

from pythonosc import dispatcher
from pythonosc import osc_server

resses = ['a','b','c','d','e'] # i work with 5 gesture types w weki/ardu

def print_volume_handler(unused_addr, args, a, b,c,d,e): # depends on num of gestures in weki
    # seems like lower the value, the higher the match
    vals = [a,b,c,d,e]
    #print(unused_addr, args[0], len(args))
    valMin = min(vals)
    #print( a, b,c,d,e, valMin )
    
    ind = vals.index(valMin) #resses.index(valMin)
    
    
    if ind > 0:
        print(ind, resses[ind])
        myStr = str.encode(resses[ind])  # send msg to arduino, ecoded to bytes
        print(
            #resses.index(valMin),
            resses[ind] )
        ser.flushInput()
        ser.write(myStr)
        time.sleep(0.1)

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/wek/outputs", print_volume_handler, "output_1")
#dispatcher.map("/wek/outputs", print_volume_handler, "xx")
#dispatcher.map("/wek/outputs/output_2", print, "out2") # doesnt work
#dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)


server = osc_server.ThreadingOSCUDPServer(
      ("127.0.0.1", 12000), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()