#Saicharan Vemuri (FiveArcher76571)
#Chopsticks
#Start: July 23, 2021

import random

def p1turn():

    p1prep = str(input("Which hand do you want to use? Or do you want to manage your own hands? (l for left, r for right, m for manage):\n"))
    p1prep = p1prep.lower()

    if (p1prep == "m"):
        #"n + (x - n)"; Ask for n and fill in blanks
        p1fingers = p1left + p1right
        varN = int(input("How many fingers do you want on your left hand?\n"))
        p1right = varN
        p1left = p1fingers - varN
    
    elif (p1prep == "l" || p1prep == "r"):
        p1atk = str(input("Which hand do you want to tap? (l for left, r for right, m for manage):\n"))
        p1atk = p1atk.lower()

        if (p1prep == "l"):
            if (p1atk == "l"):
                p2left += p1left
            elif (p1atk == "r"):
                p2right += p1left
            else:
                print("Error bruh")
        elif (p1prep == "r"):
            if (p1atk == "l"):
                p2left += p1right
            elif (p1atk == "r"):
                p2right += p1right
            else:
                print("Error bruh")
        else:
            print("Error bruh")


def p2turn():
    p2prep = str(input("Which hand do you want to use? (l for left and r for right):\n"))
    p2prep = p2prep.lower()
    p2atk = str(input("Which hand do you want to tap? (l for left and r for right):\n"))
    p2atk = p2atk.lower()

    if (p2prep == "l"):
        if (p2atk == "l"):
            p1left += p2left
        elif (p2atk == "r"):
            p1right += p2left
        else:
            print("Error bruh")
    elif (p2prep == "r"):
        if (p2atk == "l"):
            p1left += p2right
        elif (p2atk == "r"):
            p1right += p2right
        else:
            print("Error bruh")


def game():

    p1left = 1
    p1right = 1
    p2left = 1
    p2right = 1

    p1turn()
    p2turn()

    