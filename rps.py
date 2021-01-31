#Saicharan Vemuri (FiveArcher76571)
#Rock Paper Scissors
#Start: Jan. 30, 2021

import random
import time

def game(rounds):
    
    while rounds > 0:

        #Rock = 1, Paper = 2, Scissors = 3
        
        cpuhand = random.randint(1, 3)
        p1hand = str(input("What's your move? (rock, paper, scissors)\n"))
        p1hand = p1hand.lower()

        if p1hand == "rock":
            if cpuhand == 1:
                print("\nCPU: Rock\n\nTie!")
            elif cpuhand == 2:
                print("\nCPU: Paper\n\nYou Lose :(")
            elif cpuhand == 3:
                print("\nCPU: Scissors\n\nYou Win!!")
            else:
                print("\nError: Random Integer Generator must be broken or something...")
        elif p1hand == "paper":
            if cpuhand == 1:
                print("\nCPU: Rock\n\nYou Win!!")
            elif cpuhand == 2:
                print("\nCPU: Paper\n\nTie!")
            elif cpuhand == 3:
                print("\nCPU: Scissors\n\nYou Lose :(")
            else:
                   print("Error: Random Integer Generator must be broken or something...")
        elif p1hand == "scissors":
            if cpuhand == 1:
                print("\nCPU: Rock\n\nYou Lose :(")
            elif cpuhand == 2:
                print("\nCPU: Paper\n\nYou Win!!")
            elif cpuhand == 3:
                print("\nCPU: Scissors\n\nTie!")
            else:
                print("\nError: Random Integer Generator must be broken or something...")
        else:
            print("\nSorry, that wasn't a valid move. Please check your spelling and try again.")

        rounds -= 1

print("Welcome to RPS!")
p1 = input("\nWhat's your name?\n")

menu = 10

while menu != 0:

    print("\nHello" , p1 + "! Please choose an option from the menu below...")

    menu = int(input("\n1 ... Quick Match\n0 ... Exit\n\n"))

    if menu == 1:
        game(1)
    elif menu == 2:
        game(3)
    elif menu == 0:
        break
    else:
        print("Sorry, please enter one of the numbers in the menu")


input("Thank you for playing! Please press Enter to exit...")
