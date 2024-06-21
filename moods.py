def mood():
  import random
  import time
  
  good_mood = ['good','perfect','pretty''kindly','fully','neck','prime','happy','fine']
  bad_mood = ['bad','Depressed' , 'Gloomy' , 'Miserable' , 'Cheerless' , 
  'Unhappy' , 'Gloomy' , 'Sorrowful' , 'Upset' , 'Downcast' , 'Tearful' , 'Somber','sad']
  answer = input('How are you ?:')
  answer_split = answer.split()
  for char in answer_split:
    if char in good_mood :
      print('well i hope you stay like this forver ')
      print('bye')
    if char in bad_mood :
      print('Iam sory about that')
      time.sleep(1)
      print('why do you feel',char)
      mood_answer = input('tell me :')
      if mood_answer == mood_answer:
        print("Iam sorry about that . I hope you are better and never be sad")
        time.sleep(1)
        joke = input("I heard that jokes improves a person's mood. Do you want me to tell you a joke? :")
        if joke == 'yes':
          jokes = ['One day a Teacher of Science was greeting his new college class.He stood up in front of his class. and said Would everyone Who thinks he or she is stupid please stand up?After a minute or so of silence, a young girl stood up . a Well, hello there sir. So you actually think you are a moron? the professor asked.The girl replied,No sir, I just didnt want to see you standing there all by yourself' ,'Two boys were arguing when A teacher entered the room.The teacher says, “Why are you arguing? One boy answers, We found a ten dollar bill and decided to give it to whoever tells the biggest lie . You should be ashamed of your selves  said the teacher, When I was Young I didn’t even know what a lie was . The boys gave the ten dollars to the teacher', 'Man said My credit card was stolen, but I decided not to report it..When His friends asked him why you will not report it? He Said “because the thief was spending less than My wife did.' , 'Mathematics Law If you read the problem in the exam and find it easy, make sure that you solve it wrong.' , 'Two people were walking next to a tank of water. The first fell into it. The second got up and went to the tap waiting for him.'] 
          while True:
              print(random.choice(jokes))
              print('Now , I hope you will be well ')
              mood_answer2 = input('How are you now :')
              word2 = mood_answer2.split()
              for word in word2:
                if word in good_mood:
                  print('well i hope you stay like this forver ')
                  print('bye')
                  break
                
                if word in bad_mood:
                  print(' oh you look so sad ')
                  print('i will tell you another joke')
                  pass
          
        if joke == 'no':
            print('okay I hope you will be well ')
            print('bye')