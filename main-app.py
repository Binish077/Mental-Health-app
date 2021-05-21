import numpy as np
from tkinkter import *
import time

def mindful():
  set_time=float((input("How long (minutes) would you like today's meditation to be? (Default: 5 minutes) "))*60)
  if set_time=="":
    set_time=300
  print("Timer starts now")
  for i in range(set_time):
    time.sleep(1)
    set_time=set_time-1
    if set_time%5==0:
      print("Inhale/Exhale") #I'm thinking of the 4-7-8 breathing technique but I'm not sure how to implement it
    
  
  
  
