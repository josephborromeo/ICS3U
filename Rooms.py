import time
from game_functions import *

# 2D list storing all rooms in the game



# Initialize game variables
done = False




# Initial print statement
print(room_list[current_room][0])

while not done:
    player_input = input("What player_input would you like to go in - N, S, E, W? ")
    player_input = player_input.lower()
    input_parser(player_input)