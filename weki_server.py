#  https://pypi.org/project/python-osc/
import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()

from pythonosc import dispatcher
from pythonosc import osc_server

resses = ['a','b','c','d','e'] # i work with 5 gesture types w weki/ardu

#def print_volume_handler(unused_addr, args, a, b,c,d,e): # depends on num of gestures in weki
def print_volume_handler(unused_addr, args, label):
    index = int(label) -1
    myStr = str.encode(resses[index])  # msg to arduino must be encoded to bytes
    print('class', resses[index] )
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