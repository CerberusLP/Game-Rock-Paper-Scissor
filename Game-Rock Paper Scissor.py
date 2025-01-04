import os
os.system('cls')
import random

#Options

options = ["Rock", "Paper", "Scissors"]

 
user_choice = input("Choose Rock, Paper, or Scissors: ")

computer_choice = random.choice(options)

 

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)


#Conditions

if user_choice == computer_choice:

    print("Win-Win Condition!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("You win!")

else:

    print("Computer wins!")
