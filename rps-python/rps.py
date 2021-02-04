#Saicharan Vemuri (FiveArcher76571)
#Rock Paper Scissors
#Start: Jan. 30, 2021

import random

def game(rounds):
    
    p1score = 0
    cpuscore = 0
    
    while rounds != 0:

        #Rock = 1, Paper = 2, Scissors = 3
        
        cpuhand = random.randint(1, 3)
        p1hand = str(input("What's your move? (rock, paper, scissors)\n"))
        p1hand = p1hand.lower()

        if p1hand == "rock":
            if cpuhand == 1:
                print("\nCPU: Rock\n\nTie!")
                p1score = cpuscore = 1
            
            elif cpuhand == 2:
                print("\nCPU: Paper\n\nYou Lose :(")
                cpuscore += 1
            
            elif cpuhand == 3:
                print("\nCPU: Scissors\n\nYou Win!!")
                p1score += 1
            
            else:
                print("\nError: Random Integer Generator must be broken or something...")
        
        elif p1hand == "paper":
            if cpuhand == 1:
                print("\nCPU: Rock\n\nYou Win!!")
                p1score += 1
            
            elif cpuhand == 2:
                print("\nCPU: Paper\n\nTie!")
                p1score = cpuscore = 1
            
            elif cpuhand == 3:
                print("\nCPU: Scissors\n\nYou Lose :(")
                cpuscore += 1
            
            else:
                   print("Error: Random Integer Generator must be broken or something...")
       
        elif p1hand == "scissors":
            if cpuhand == 1:
                print("\nCPU: Rock\n\nYou Lose :(")
                cpuscore += 1
            
            elif cpuhand == 2:
                print("\nCPU: Paper\n\nYou Win!!")
                p1score += 1
            
            elif cpuhand == 3:
                print("\nCPU: Scissors\n\nTie!")
                p1score = cpuscore = 1
            
            else:
                print("\nError: Random Integer Generator must be broken or something...")
        
        else:
            print("\nSorry, that wasn't a valid move. Please check your spelling and try again.")

        rounds -= 1
    
    return [p1score, cpuscore]


def scoring(scores):

    if scores[0] < scores[1]:
        print("\nSorry, you lost the game...\nBetter luck next time!")

    elif scores[0] == scores[1]:
        print("\nFinal Round...\n\n")
        game(1)
    
    elif scores[0] > scores[1]:
        print("\nYou win the game!! Congratulations!!!")


print("Welcome to RPS!")
p1 = input("\nWhat's your name?\n")

menu = 10

while menu != 0:

    print("\nHello" , p1 + "! Please choose an option from the menu below...")

    try:
        menu = int(input("\n1 ... Quick Match\n2 ... Best 2 out of 3\n0 ... Exit\n\n"))
    except:
        print("Sorry, please enter a number.")
        menu = int(-1)

    if menu == 1:
        game(1)
    elif menu == 2:
        scoring(game(2))
    elif menu == 0:
        break
    elif menu == -1:
        print("Returning to menu...\n")
    else:
        print("Sorry, please enter one of the numbers in the menu.")


input("Thank you for playing! Please press Enter to exit...")
