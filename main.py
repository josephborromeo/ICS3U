from game_functions import *

# Main game loop
def main():
    # Initialize game variables
    done = False

    # Initial intro print statements
    print("You wake up in a random building with no recollection of how you got here.")
    time.sleep(0.5)  # sleep = 4
    print("You have an uneasy feeling about this place and want to get out of here as soon as possible... \n")
    time.sleep(0.5)  # sleep = 5
    print(room_list[current_room][0])

    print('\nType /help for a list of in game commands')
    while not done:
        player_input = input("\nWhat direction would you like to go in - N, S, E, W? ")
        player_input = player_input.lower()
        input_parser(player_input)
main()