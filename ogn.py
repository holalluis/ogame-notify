#!/usr/bin/env python3
'''
  notify helper for ogame.
  notifies next action based on current resources,
  target resources and production
'''
import math
import platform
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
  tens = math.floor(actual + i*prod/3600) #recursos augmentant
  queden_s = segons-i; #segons
  queden_m = math.floor(queden_s/60) % 60; #minuts
  queden_h = math.floor(queden_s/3600); #hores
  print("Tens ",tens,"/",preu,": falta ",
    queden_h,"h ",
    queden_m,"m ",
    queden_s%60,"s...",
    sep='',
    end='\r')
  time.sleep(1)

print('\nNext action:',action)

#sound
subprocess.run(['mpv',"sound.mp3"])

#notification depending on OS
if platform.system()=='Darwin':
  subprocess.run(['osascript','-e', 'display notification "'+action+'" with title "ogame"'])
elif platform.system()=='Linux':
  subprocess.run(['notify-send',"ogame",action])
