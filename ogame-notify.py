#!/usr/bin/python3
'''
  notify next action based on current resources, target and
  production
'''
import math
import subprocess
import sys
import time

#check inputs
if len(sys.argv)<5:
  print("Us: ",sys.argv[0],"[current]","[price]","[production per hour]","[next action]")
  sys.exit()

#inputs
actual = int(sys.argv[1]) #current resource units
preu   = int(sys.argv[2]) #price of target
prod   = int(sys.argv[3]) #production per hour
action = sys.argv[4]      #next action

#compute seconds
segons=math.floor((preu-actual)/prod*3600); #seconds until next action

#show continuous indication
for i in range(segons):
  tens = math.floor(actual + i*prod/3600)
  print("You have",tens,"/",preu,":",segons-i,"seconds...",end='\r')
  time.sleep(1)

#end: create notification and play sound
print('\n\n',action)
subprocess.run(['notify-send',"ogame",action])
subprocess.run(['mpv',"sound.mp3",action])
