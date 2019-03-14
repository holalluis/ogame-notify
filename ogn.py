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
  tens = math.floor(actual + i*prod/3600)
  print("Tens",tens,"/",preu,":",segons-i,"segons...",end='\r')
  time.sleep(1)

print('\n\nNext action:',action)

#play sound
subprocess.run(['mpv',"sound.mp3",'/dev/null'], capture_output=True)

#create notification
if platform.system()=='Darwin':
  #OS X
  subprocess.run(['osascript','-e', 'display notification "'+action+'" with title "ogame"'])
else:
  #Other
  subprocess.run(['notify-send',"ogame",action])
