import time
from math_assistant import math_assistant
from morse_code import morse_code
from guesses import guess_passwords
from moods import mood
from learn_python import lists_python

names = ['mostafa' , 'Mostafa' , 'MOSTAFA']
name = str(input('Hellow Iam jarvis please enter your name :'))
if name in names :
  print('welcome back' , name)
  time.sleep(1)
  answer2 = input('Do you want help :')
  if answer2 == 'yes':
    print('okay')
    print('1- mathematics----2- translate into morse code ----3- guess passwords  4- learn python')
  if answer2 == 'no':
    print('I feel you are sad')
    mood()
else:
  print('hello' , name)
  time.sleep(2)
  print('Iam jarvis I can help you in different things')
  time.sleep(2)
  answer2 = input('Do you want help :')
  if answer2 == 'yes':
    print('okay')
    print('1- I can help you in mathematics------ 2- I can translate to morse code------ 3-I can guess any thing 4- i can help you in learning python')
  if answer2 == 'no':
    print('I feel you are sad')
    mood()

if answer2 == 'yes':
  while True:
      answer = input ('enter the number of the option do you want :')
      if answer == '1':
        math_assistant()
      elif answer == '2':
        morse_code()
      elif answer == '3':
        guess_passwords()
      elif answer == '4':
        lists_python()
          
      time.sleep(1)
      answer1 = input ('    ////do you want any thing else :')
      if answer1 == 'yes':
        pass
      elif answer1 == 'no':
        print('okay....bye', name)
        break