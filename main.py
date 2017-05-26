#-------------------------------------------------------------------------------
# Name: main.py
# Purpose:	Play Adventure Prison Escape - The best adventure game known to man
#
# Author:	Borromeo.J
#
# Created:	11/05/17
# #------------------------------------------------------------------------------

# Import other file with all the game functions
from game_functions import *

# Main game loop
def main():
    # while loop variable
    done = False

    # Initial intro welcome statements
    text_typer("You wake up in a random building with no recollection of how you got here.\n", 0.06)
    time.sleep(1)
    text_typer("You have an uneasy feeling about this place and want to get out of here as soon as possible... \n\n", 0.06)
    time.sleep(1)
    text_typer(room_list[current_room][0] + '\n', 0.02)

    print('\nType /help for a list of in game commands')

    # Main game loop
    while not done:
        player_input = input("\nPlease input a command: ")
        player_input = player_input.lower()
        input_parser(player_input)
main()