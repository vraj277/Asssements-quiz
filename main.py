import random #<This is self explanatory because it uses random shuffle to import random questions from the list below.


#Name

print("|=============================================================================|")  
#This section below asks for the user's name. I've used the while true function to ensure that it runs rapidly (loops) if the user enters in an invalid name, such as a number, which is  why it's in while loop.
while True:
    try:
        name_1 = input("|* Please enter your name: |")
        if name_1.isalpha(): #<This method checks if the user has written their name in alphabetical order, and if they haven't, it breaks it and outputs the error message below. Using the while loop, the code prints out the name statement again following the error statement.
          break
        else:
          print("|---------------------------------------------------------------------|")
          print("|         Please enter a name with letters only, and dont leave empty |")
          print("|---------------------------------------------------------------------|")
          
      
    except ValueError:
        print("|        Please Enter a name with letters only, and dont leave empty            |")

print("|=============================================================================|") 

#Menu

def main_menu():#This function stores whatever I want into the menu statement in addition to defining it. This makes things easier since all I have to do now is call welcome main_menu(), and it will do all of the tasks in this function for me.
  print("|*****************************************************************************|")
  print("|                                                                             |")
  print("|                     WELCOME TO THE MATH QUIZ 2022                           |")
  print("|                                                                             |")
  print("|*****************************************************************************|")
  print("|                       Please select an option:                              |")
  print("|*                                                                           *|")
  print("|                       1. Play Math quiz                                     |")
  print("|                       2. Know the rules                                     |")
  print("|                       3. Quit                                               |")
  
  print("|*                                                                           *|")
  print("|*****************************************************************************|")
  print("|=============================================================================|")
#This part below prompts the user to choose an option. I utilised the while true function to ensure that it runs rapidly (loops) if the user fills in an inaccurate number that does not meet my if choice statement.
  while True: 
    try:
       choice = input("|*      Enter 1,2 or 3: |") #This part below prompts the user to choose an option. I utilised the while true function to ensure that it runs rapidly (loops) if the user fills in an inaccurate number that does not meet my if choice statement.
 #<This portion compares the user's answer that  is in variable choice; if the user's answer does not match 1, 2, or 3, they receive a value error message; if they do, they continue. 
       if choice == '1': 
           break
       elif choice == '2':
           break
       elif choice == '3':
           break
        
       else: 
         print("|----------------------------------------------------------------------|")
         print("|                     Not a Valid Integer! Please Only Enter 1, 2 or 3 |" )
         
         print("|----------------------------------------------------------------------|")
    except ValueError:
        print("|                     Not a Valid Integer! Please Only Enter 1, 2 or 3 |" )

#This section below contains codes that I want quiz to run  if they type in 1,2, or 3. For example, if they write 1, the quiz will lead them to the welcome statement , which is part of the welcome MCQ quiz function (). If 3 , it prints "thank you" and then exits. If the answer is 2, it will publish everything that is related to the that option.
  
  if choice == "1":
    welcome_MCQ_quiz()
  elif choice == "3":
    print("Thanks for Playing :) !")
    quit()
  elif choice == "2":
    print("|=============================================================================|")
    print("|*****************************************************************************|")
    print("|                     Here are 3 simple rules :                               |")
    print("|*                                                                           *|")
    print("|                     1. No cheating                                          |")
    print("|                     2. Only calculators are  allowed if necessary           |")
    
    print("|                     3. Have Fun!!                                           |")
    print("|*                                                                           *|")
    print("|*****************************************************************************|")
    print("|=============================================================================|") 
    input("|*     Press Enter To Continue...")
    print("|=============================================================================|") 
    welcome_MCQ_quiz() #< After clicking enter, this function instructs the quiz to direct them straight to welcome_mcq_quiz function.
  








#Welcome 

def welcome_MCQ_quiz(): #<This function not only defines the welcome statement, but it also saves whatever I want within it. This simplifies things since all I have to do now is call welcome MCQ quiz(), and it will perform all of the tasks in this function.
  print("|=============================================================================|") 
    
  print("|*****************************************************************************|")


  print("|*                                                                           *|")
  print("|                   Hello {}, Welcome to My Math Quiz 2022.                    |\n|            Please enter in your answer if the program prompts you to do so, |\n|         and please read the rules. Please note that this quiz is designed   |\n|       specifically for year 11 students, so if you are in year 10 or below  |\n|          and/or above, you will either find it tough or simple.             |\n|                       \033[4mNote\033[0m -'^' = to the power of                           |\n|                          Good Luck have fun!!                               |" .format(name_1)) #<variable is substituted by this .format function. Because it has this "{}"which implements that specific variable answer in that specific section, it will place their name after the "hello" in this example (name 1 is where the code asks for the user name).
  
  
  print("|*****************************************************************************|")
  print("|=============================================================================|") 
  input("|*      Press Enter To Continue To Start Questions...")
  play_MCQ_quiz() #< This function is called play_MCQ_quiz, and it starts with questions and records all the necessary information, such as value errors, asking the user to input their response, and double-checking their answer against my dictionary values. This simplifies things since all I have to do now is add a define statement, and when I call it, it will perform all of the tasks that are included within that define function.
  print("|=============================================================================|") 



#starting  of the quiz
 


#With the help of a dictionary, this variable below contains all of my math questions. My keys and values are stored in a dictionary; in this example, my keys are math questions included within the variable questions, and the value is the answers to those math questions.
questions = {'|*               Solve Following Equation   \n|         2x^2 – 3xy when x = –3 and y = 4 \n|    a: 54 \n|    b: 69 \n|    c: 52' : 'a' ,
'|*              Solve Following Equation                            \n|     w^4 – 18w^2 + 81 = 0 \n|    a: -9, 9  \n|    b: -3. 3\n|    c: -6x 6 \n' :  'b' , 
'|*               Solve the inequality \n|         (3x + 2)(2x – 1) ≤ (6x + 1)(x – 3)\n     a: x < -1/8\n|    b: 18x < -1 \n|    c: x < -1/18 \n' : 'c' , '|*               Solve the equation \n|         x+2/3 - 2x-1/5 = 1\n    a: x = -1 \n|    b: x = 2 \n|    c: x = -2 \n' : 'c' ,'|*         Solve the equation \n|     2/x-3 - 2/x-1 = 3/x+5 \n|    a: x = 7 \n| b: x = 6\n|    c: x=8 \n' : 'a' ,'|*               Calculate the Probability   \n|         Levi’s father says that, when he was the same age, his chance of    |\n|scoring was 60% If Levi’s father had taken 200 shots when he was the same age|\n| how many shots would he have scored on? \n|    a: around 120 \n|    b: around 140 \n|    c: around 100' : 'a' ,'|*               Calculate the Probability   \n|         75% of homes on the national power supply in New Zealand are in the |\n|North Island. The rest are in the South Island.70% of homes in the North     |\n|Island and 80% of homes in the South Island use electricity for their heating|\n|Calculate the probability that a home selected randomly across New Zealand is|\n|on the national power supply in the North Island AND uses electricity for    |\n| heating. \n|    a: 21/40 \n|    b: 25/40 \n|    c: 36/40' : 'a' ,'|*               Solve following problem  \n|Leo is laying square concrete tiles for his deck. He starts with laying them |\n|down to form a square pattern, but his friend thinks it would be better if   |\n|they were laid out to form a rectangle. He changes his layout to make the    |\n|length of the deck 6 tiles longer, and the width of the deck 4 tiles shorter.|\n|He finds he needs 2 extra tiles to complete the rectangular pattern.How many |\n| tiles did he have to start with? \n|    a: 13 \n|    b: 169 \n|    c: 48' : 'b' ,'|*               Solve following problem   \n|         Tane and Pete are raising funds for their sports trip. Between them |\n|they need to raise $1000.There are only 5 weeks until they need the money.   |\n|Tane gets paid $15 an hour, and Pete gets paid $16 an hour as he has more    |\n|experience. Between them they work for a total of 13 hours each week.What is |\n|the average number of hours that each of them work per week if they are to   |\n|have exactly the amount of money they need? \n|    a: Pete = 5h & Tane = 10h \n|    b: Pete = 4h & Tane = 7h \n|    c: Pete = 5h & Tane = 8h' : 'c' ,'|*               Solve following problem    \n|         Mere gives some clues so that her secret number can be calculated.  |\n|She says, “When 20 is divided by my secret number and then 7 is added to this|\n|answer, this gives a solution of 2.” What is Mere’s secret number?           | \n|    a: -8 \n|    b: -4 \n|    c: 8' : 'b' ,}


def play_MCQ_quiz(): #<This is the function that checks for errors, prints keys from the dictionary, and prompts the user for a response. I've put everything in a define statement so that I can just say play play_MCQ_quiz() and it will run everything within it. This function prints out math questions, then asks the user for a response, and then verifies whether it's accurate or wrong.
 score = 0 #<This is a scoring system variable, and their current score is 0.
  
 k = list(questions)
 random.shuffle(k)#< This is self-explanatory since it radom shuffles the variable "k" that has my list of questions.
 for key in k:#<This function calls the keys (math questions) in my variable "questions" through the variable "k," which is the variable that randomises the order of my questions.__package__
  print("|*****************************************************************************|")
  print("|                                                                             |")
  print(key)#<now this prints those keys
  print("|                                                                             |")
  print("|*****************************************************************************|")
  print("|=============================================================================|")
 
#this section below checks if the user has entered in coreect format of  answer for example checks if they have enter a, b or c if not any, it gives them an error.
   
 
  while True: 
    try:
       user_answer = input("|*     Enter A, B or C: |").lower().strip()  #<The variable user answer stores the replies. Lower and strip prevent the code from receiving the wrong response since lower converts the user's answer to lower case, which matches my dictionary entry, ensuring accuracy, and strip prevents additional spaces if the user has mistakenly inserted one.
       if user_answer == 'a': 
           break
       elif user_answer == 'b':
           break
       elif user_answer == 'c':
           break
        
       else: 
         print("|---------------------------------------------------------------------|")
         print("|        Please only Enter A, B or C and dont leave empty             |")
         print("|---------------------------------------------------------------------|")
    except ValueError:
      print("|        Please only Enter A, B or C and dont leave empty                   |")


  print("|=============================================================================|")
  if questions.get(key) == user_answer:#This section instructs the code to verify if the user's input matches the dictionary value; if so, the result will be correct; if not, the result will be wrong.
          print("                                          |-------------------------------|     ")
          print("                                          |         Correct!              |     ")  
          print("                                          |-------------------------------|     ")
          score =  score + 1 #If the user gets it right, it adds a point to their score, and each question is worth one point.
  else:
          print("                                          |-------------------------------|     ")
          print("                                          |        Incorrect :(           |     ")
          print("                                          |-------------------------------|     ")
 print("| Thanks for taking the quiz; I appreciate you taking the time to do so, and I|\n| hope you learnt something from it.                                          |\n| Your Final Score is:  " + str(score)) #< prints out their total score at the end.






main_menu()


