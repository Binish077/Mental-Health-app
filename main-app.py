import numpy as np
# If you are importing everything from tkinter, line 4 better than line 3
# from tkinkter import *
import tkinter
import time
import random
import diary as diary
import illnesses_info_page as ill
import quiz as quiz

def mindful():
  minutes=input("How long (minutes) would you like today's meditation to be? (Default: 5 minutes) ")
  if minutes=="":
    set_time=300
  else:
      set_time=float(minutes)*60

  print("Timer starts now\n")
  t1=set_time
  t2=0
  for i in range(int(set_time/21)):
    t2=time.process_time()
    print("Take a deep breath")
    for i in range(4):
        time.sleep(1)
        t1=t1-1
        t2=t2+1
    print("Hold your breath...")
    for i in range(7):
        time.sleep(1)
        t1=t1-1
        t2=t2=1
    print("Slowly exhale\n")
    for i in range(8):
        time.sleep(1)
        t1=t1-1
        t2=t2+1
        
    if t1%45==0:
        #a few relaxing statements to be printed every minutes
        s1="Let go of any worries and thoughts you might have"
        s2="Focus on your breathing"
        s3="You're doing well"
        s4="Relax your muscules"
        quotes=[s1,s2,s3,s4]
        print(random.choice(quotes)+"\n")

  if set_time-t2>0:
      print("\nUse these last seconds to loosen your muscules and focus on the quality of your breathing\n")
      for i in range(int(set_time-t2)):
          time.sleep(1)

  print("That is the end of the meditation, you will be directed to the home page now") 
#Asks the user what they would like to do

def main():

    while True:
        print("===============================================================")
        print("Welcome to Incremental, what would you like to do today?")
        print("a) Journal\nb) Illnesses information page\nc) Take a quiz\nd) Meditate\n")
        user_choice=input("Enter your answer (a,b, or c) Press ENTER to exit: ")
        print("===============================================================")
        print("\n")
        if user_choice=='a':
            diary.execute_diary()
            print("\n")

        elif user_choice=='b':
            ill.execution()
            print("\n")

        elif user_choice=='c':
            quiz.execute_quiz()
            print("\n")
        
        elif user_choice=='d':
            mindful()
            print("\n")
    
        elif user_choice=="":
            print("Thank you for using Incremental!")
            break
    
        else:
            print("Please enter a valid input\n")

main()
    
    
