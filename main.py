import random

questions = { '| Question one  \n| 2x(3x+4) \n| a: 6x^2+8x \n| b: 5x^2+8x\n| c: 5x+8x\n' : 'a' , '| Question 2\n| 9x(12x+18) \n a: 21x^2+27x a\n b: 108x^2+162x\n c: 9x+30x \n' :  'b' , 'Question 3 \n a: answer a\n b: answer b\n c: answer c \n' : 'c' }

  


def play_MCQ_quiz():

  

  

  score = 0
#add error handling
  for key in questions.keys():
      print("|*******************************|")
      print(key )
      user_answer = input("Enter A, B or C:").lower().strip()
      print("|*******************************|")
      if questions.get(key) == user_answer:
          print("|         Correct!              | ")
          score =  score + 1
      else:
          print("|        Incorrect :(           | ")
      
  print("| Your Final Score is: " + str(score))
      



def welcome_MCQ_quiz():
   
  print("|*******************************|")
  name_1 = input("|* Please enter your name: |")
  print("|*Hello {}, Welcome to My       |\n| Math quiz 2022 please type in |\n| answer if the AI ask you to   |\n| and please read the rules,note|\n| that this is quiz is purely   |\n| made for year 11 students so  |\n| if you are from year 10 or    |\n| below and/or above you will   |\n| either find it difficult or   |\n| easy, thanks and have fun.    |".format(name_1))
  print( "| \033[4mNote\033[0m -'^' = to the power of   |")
  
  print("|*******************************|")

  play_MCQ_quiz()


  


def main_menu():
  print("|*******************************|")
  print("| WELCOME TO THE MATH QUIZ 2022 |")
  print("|*******************************|")
  print("| Please select an option:      |")
  print("|*                             *|")
  print("| 1. Play Math quiz             |")
  print("| 2. Know the rules             |")
  print("| 3. Quit                       |")
  print("|*******************************|")
  choice = input("| Enter 1, 2, or 3: ")
  
  if choice == "1":
      welcome_MCQ_quiz()
  elif choice == "3":
    print("Thanks for Playing :) !")
    quit()
  elif choice == "2":
    print("| Here are 3 simple rules       |")
    print("| 1. No cheating                |")
    print("| 2. only calculators are       |")
    print("|    allowed if necessary       |")
    print("| 3. Have Fun!!                 |")
    welcome_MCQ_quiz()

main_menu()
play_MCQ_quiz()

  
  



  

