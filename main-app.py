import numpy as np
# If you are importing everything from tkinter, line 4 better than line 3
# from tkinkter import *
import tkinter
import time
import random

def mindful():
  minutes=input("How long (minutes) would you like today's meditation to be? (Default: 5 minutes) ")
  if minutes=="":
    set_time=300
  else:
      set_time=float(minutes)*60

  print("Timer starts now")
  for i in range(int(set_time)):
    time.sleep(1)
    set_time=set_time-1
    if set_time%5==0:
      print("Inhale/Exhale\n") #I'm thinking of the 4-7-8 breathing technique but I'm not sure how to implement it
    if set_time%45==0:
        #a few relaxing statements to be printed every minutes
        s1="Let go of any worries and thoughts you might have"
        s2="Focus on your breathing"
        s3="You're doing well"
        s4="Relax your muscules"
        quotes=[s1,s2,s3,s4]
        print(random.choice(quotes)+"\n")
mindful()