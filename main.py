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
    welcome_statement()
  elif choice == "3":
    print("Thanks for Playing :) !")
    quit()
  elif choice == "2":
    print("| Here are 3 simple rules       |")
    print("| 1. No cheating                |")
    print("| 2. Dont use calculator only   |")
    print("|    if necessary               |")
    print("| 3. Have Fun!!                 |")

main_menu()

# welcome statment 
def welcome_statement():
  print("Hello, Welcome to My Math quiz 2022, please type in answer if the ai ask you to and please read the rules, note that this is quiz is purely made for year 11 students so if you are from year 10 or below and/or above you will either find it difficult or easy, thanks and have fun.")
  

