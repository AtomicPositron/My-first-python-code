import time
import random

from numpy import count_nonzero
person = {
   "Name": "",
   "Email": "",
   "Password": "",
   "score": 0
}
modes = ["Easy","Hard"]
def call():
     person["Name"] = input("What is your Name: ")
     person["Email"] = input("What is your Email: ")
     person["Password"] = input("What is your Password: ")
     verification_all(0)
def home():
     print("Welcome to my program "+person["Name"])
     time.sleep(2)
     print("pick a mode")
     print("1: "+modes[0]+"\n"+"2: "+modes[1])
     answer = input("Which number: ")
     if int(answer) == 1:
        easy()
     elif int(answer) == 2:
        hard()
     else:
       print("wrong command")
       home()
def verification_all(t):
      if  t >= 0 :
        if person["Name"] == "" and person["Email"] == "" and person["Password"] == "":
          print("please fill the form complete")
          call()
        else:
          home()
      else:
         home()
  
       
def easy():
    print("There are ten rounds")
    count = 1
    tries = 1
    inc = 10
    num =1
    score = 0
    speed = 2
    while count > 0:
       time.sleep(2)
       print("try to survive")
       num_one = str(random.randrange(num,inc))
       num_two = str(random.randrange(num,inc))
       fact = num_one +" + "+num_two
       tries += 1
       if tries % 3 == 0:
          inc += 10
          num += 10
          speed -= 0.5
       print(fact)
       answer = input("Whats your answer: ")
       if answer == "Q":
          count = -1
          print("Your score is: "+str(score))
          verification_all(-1)
       elif int(answer) == int(num_one)+int(num_two):
          score += 1
          print("correct 😁")
       else:
          print("incorrect 😒")
       if count == 10:
          count = -1
          print("sorry but that is how much we can give")
          print("Your score is: "+str(score))
          verification_all(-1)
       print("......\n......")
       
       count += 1
    
       
def hard():
    print("There are ten rounds")
    count = 1
    tries = 1
    inc = 40
    num =1
    score = 0
    speed = 3
    while count > 0:
       time.sleep(2)
       print("try to survive")
       num_one = str(random.randrange(num,inc))
       num_two = str(random.randrange(num,inc))
       fact = num_one +" + "+num_two
       tries += 1
       if tries % 5 == 0:
          inc += 10
          num += 10
          speed -= 0.5
       print(fact)
       answer = input("Whats your answer: ")
       if answer == "Q":
          count = -1
          print("Your score is: "+str(score))
          verification_all(-1)
       elif int(answer) == int(num_one)+int(num_two):
          score += 1
          print("correct 😁")
       else:
          print("incorrect 😒")
       if count == 10:
          count = -1
          print("sorry but that is how much we can give")
          print("Your score is: "+str(score))
          verification_all(-1)
       print("......\n......")
       
       count += 1
    
verification_all(0)
