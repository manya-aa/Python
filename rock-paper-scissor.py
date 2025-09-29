import random

def who_win(your_choice,comp_choice):
    if your_choice==comp_choice:
       return "So, You Won!"
    elif (your_choice=="rock" and comp_choice=="paper")\
        or (your_choice=="paper" and comp_choice=="scissor")\
        or (your_choice=="scissor" and comp_choice=="rock"):
        return "So, You Lose!"
    else :
        return "So, You Won!"

your_choice=input("Enter your choice: ")
comp_choice=random.choice(["rock", "paper", "scissor"])
winner=who_win(your_choice,comp_choice)
print("You chose "+your_choice)
print("Computer chose "+comp_choice)
print(winner)