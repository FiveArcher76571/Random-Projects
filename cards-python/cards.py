#Saicharan Vemuri (FiveArcher76571)
#Cards
#Made using the tutorial at https://projects.raspberrypi.org/en/projects/deck-of-cards/
#Started June 26th, 2021

import random

class Card:
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def __repr__(self):
        return self.num + " of " + self.suit


mycard = Card("hearts", "6")
print(mycard)

input ("\n\nPress Enter to exit...")