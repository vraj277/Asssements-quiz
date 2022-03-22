def play_MCQ_quiz():
  print("|*******************************|")
  name_1 = input("|* Please enter your name: |")
  print("|*Hello {}, Welcome to My Math   |\n| quiz 2022 please type in      |\n| answer if the AI ask you to   |\n| and please read the rules,note|\n| that this is quiz is purely   |\n| made for year 11 students so  |\n| if you are from year 10 or    |\n| below and/or above you will   |\n| either find it difficult or   |\n| easy, thanks and have fun.    |".format(name_1))







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
      play_MCQ_quiz()
  elif choice == "3":
    print("Thanks for Playing :) !")
    quit()
  elif choice == "2":
    print("| Here are 3 simple rules       |")
    print("| 1. No cheating                |")
    print("| 2. only calculators are       |")
    print("|    allowed if necessary       |")
    print("| 3. Have Fun!!                 |")

main_menu()

# welcome statment 



  

