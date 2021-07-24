#Saicharan Vemuri (FiveArcher76571)
#Started: Feb. 1, 2021
#cet????

print("Hello! Welcome to cet!!\n\n")
name = input("Before we start, what would you like to name cet?\n")

def petcet():

    pets = True

    petcounter = 0

    while pets:

        print("\nYou pet" , name + "...\n" + name , "is fluffy.\n")
        petcounter += 1
        print("Pet Counters:" , petcounter)

        if petcounter == 10:
            print("You have reached new petting heights with" , name + "." , name , "seems to want more pets!\n\n")
        
        if petcounter == 100:
            print("You have a lot of time on your hands, don't you....\n\nAre you sure you want to spend this much time on this?\n\nWell, in any case, I'm glad you're having fun! :)")


        morepet = input("Would you like to pet again? (Y/N)\n")

        if morepet.lower() == "y":
            pets = True

        elif morepet.lower() == "n":
            pets = False

        else:
            print(name , "doesn't understand your response. Try again...\n")

def feedcet():
    
    print("What would you like to feed" , name + "?\n")

    food = input("1 ... Kibble\n2 ... Nature's Domain from Costco\n3 ... Fruits\n4 ... Thanksgiving leftovers\n5 ... Generic Food Substance\n")

    try:
        food = int(food)
    except:
        print(name , "doesn't recognize what you're giving, and questions your decisions...\n")

    if type(food) == str:
        return 0

    if food >= 1 and food <= 5:
        print(name , "eats the food, but you can't tell if" , name , "likes it or not. You question your decision, but decide to move on...\n")

    elif food < 1 or food > 5:
        print("Have you given" , name , "anything? Your decision doesn't have any food...\n")

cet = 10

while cet != 0:

    print("What would you like to do with" , name + "?\n\n1 ... Pet" , name + "\n2 ... Feed" , name + "\n3 ... Pick up" , name + "\n0 ... Leave" , name + "\n")
    cet = input()
    try:
        cet = int(cet)
    except:
        print(name , "doesn't like words or decimals right now. Only numbers pls...\n")

    if cet == 1:
        petcet()
    
    elif cet == 2:
        feedcet()
    
    elif cet == 3:
        print("Actually, quantum physics forbids this...\n")

    elif cet == 10:
        print("\n")
    
    elif cet == 0:
        break

    else:
        print(name , "doesn't like it when you type that. Please type an option that's given.\n")

print(name , "has enjoyed your presence. Have a nice day.")

input("cet wants you to press Enter before you go...")