#!/usr/bin/python3
import sys
import math
import time
import subprocess

#check input
if len(sys.argv)<5:
  print("Us: ",sys.argv[0],"[actual]","[preu]","[produccio per hora]","[next action]")
  sys.exit()

#name inputs
actual = int(sys.argv[1]) #unitats que tens
preu   = int(sys.argv[2]) #unitats que vols tenir
prod   = int(sys.argv[3]) #prod per hora
action = sys.argv[4]      #proxima accio

#calculs
segons=math.floor((preu-actual)/prod*3600); #segons que falten per poder fer accio

#mostra indicador continu
for i in range(segons):
  tens = math.floor(actual + i*prod/3600);
  print("Tens",tens,"/",preu,": ",segons-i,"segons...",end='\r')
  time.sleep(1)

#final
print()
print()
print(action)

#avisa amb notificacio i so
subprocess.run(['notify-send',"ogame",action]);
subprocess.run(['mpv',"sound.mp3",action]);
