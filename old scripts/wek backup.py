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
    if not ser.readline():
        print('-')
    raw = ser.readline().decode()
    #if raw:
    print(raw);
    #if raw.isdigit() == True:
    '''if is_number(raw):
        val = float( int(raw) )
        #print(val)
        # it comes as bytes, this decodes it to string 
        #val = int(ser.readline(),10) #
        #if val>35:
        weki.send_message("/wek/inputs", val )'''
    #else
        
    
    
        
        
    #if val > 200:
        #ser.flushInput()
        #myStr = str.encode("b")  # sed msg to arduino
        #ser.write(myStr)
    #    time.sleep(0.1)
    