import time
from Rooms import *

def commands(input):
    '''
    Displays Commands when the user types them in
    All commands: /help, /search, /hp, /inv, /time
    :param input: 
    :return: 
    '''
    input = input.split(" ")
    # Help Command
    if input[0] == "/help":
        print("\t\tCommands\n---------------------------------------\n/help\tPrints help dialog\n/search\tSearches the room for entities\n/hp\t\tDisplays your current and max HP\n/inv\tDisplays your current and max inventory\n/time\tDisplays the current in game time")
    # Search Command
    elif input[0] == "/search":
        print("Searching Room", end = '')
        time.sleep(0.25)
        print ('.', end = '')
        time.sleep(0.25)
        print('.', end ='')
        time.sleep(0.25)
        print('.', end ='')
    #
    elif input[0] == "/hp":
        pass
    elif input[0] == "/inv":
        pass
    elif input[0] == "/time":
        pass

    else:
        print("That is not a valid input, type /help for a list of commands")

def input_parser(input):
    global current_room, room_list
    if input == 'n' or input == 'north':
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    elif input == 'e' or input == 'east':
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    elif input == 's' or input == 'south':
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    elif input == 'w' or input == 'west':
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    else:
        commands(input)