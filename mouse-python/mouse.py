#Saicharan Vemuri (FiveArcher76571)
#Started Apr. 7, 2021
#Mouse Control Test
#Requires mouse module (needs to be installed)

import mouse

print(mouse.get_position())

mouse.move(100, 100, absolute=False, duration=0.2)

print(mouse.get_position())

input("Press Enter to exit...")