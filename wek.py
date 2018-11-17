import serial
ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()
#serSend = serial.Serial('/dev/ttyACM0',14400)

#import argparse
import random
import time
import math

from pythonosc import osc_message_builder
from pythonosc import udp_client


weki = udp_client.SimpleUDPClient("127.0.0.1", 6448)
#weki = udp_client.SimpleUDPClient("127.0.0.1", 6448)

# used in checking who sent serial msg
def is_number(s):
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False
run = 1
while run:
    
    #if ser.readline():
        raw = ser.readline().decode()    
        #print(raw);
        
        # if incoming isn't array of vals, ignore
        if raw[0] != '[':
            print(raw, 'not arr')
            
        else:
            print('array')
            vals = raw.replace('\r', '').replace('\n','')
            vals = vals.replace('[','').replace(']','').replace('\r', '').replace('\n','')
            vals = vals.split(',')
            for i in range(len(vals)):
                vals[i] = float(vals[i])#
            print(vals)
            weki.send_message("/wek/inputs", vals )
   # else:
    #    print('no serial')
    