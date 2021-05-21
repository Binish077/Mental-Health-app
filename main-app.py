import numpy as np
# If you are importing everything from tkinter, line 4 better than line 3
# from tkinkter import *
import tkinter
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
      print("Inhale/Exhale") #Look at 'breathNotes' file 
mindful()