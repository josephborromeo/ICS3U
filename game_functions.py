import time, random
from Rooms import *

# Define Game Variables
player_name = input("Hello Adventurer! What is your name: ")

# In game time
start_time = time.time()

# Starting HP
HP = 10

# Starting Attack
attack = 2

# Starting inventory Space
max_inventory = 2

# Counts how many items the player is currently holding
def inventory_count():
    inventory_amount = 0
    for i in player_inventory():
        inventory_amount += i
    return inventory_amount

def game_time():
    current_time = time.time() - start_time
    hour = int(current_time // 60)
    mins = int(current_time - hour*60)
    if hour >= 24:
        hour = hour-24
    if hour >= 0 and hour < 12:
        print("The Current time is: " + str(hour) + ":" + str(mins).zfill(2) + " am")
    elif hour == 12:
        print ("The Current time is: " + str(hour) + ":" + str(mins).zfill(2) + " pm")
    elif hour > 12 and hour < 24:
        print("The Current time is: " + str(hour-12) + ":" + str(mins).zfill(2) + " pm")

def display_items():
    if room_list[current_room][7] == None:
        print (found_none[random.randint(len(found_none))])
    else:
        print ("Found\n------")
        for i in room_list[current_room][7]:
            if i == 'key':
                print ("A Key")
            elif i == 'enemy':
                pass
            elif i == 'bag':
                print ('A Key')
            elif i == 'food':
                print ('Food')
            elif i == 'key_card':
                print ('A Key Card')
            elif i == 'weapon':
                print ('A Weapon')
            else:
                print ('Something goofed')

def check_for_enemies(room):
    # if enemies = false, then pass
    pass

def weapon_chooser():
    pass

def split_desc(room):
    decription = room_list[current_room][0].split('\n')
    print(decription[0] + '\n' + decription[-1])

def display_description(room):
    if room_list[current_room][5] == False:
        print (room_list[current_room][0])
        room_list[current_room][5] = True
    else:
        split_desc(room)


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
        print("Searching Room...\n")
        time.sleep(0.5)
        display_items()
    elif input[0] == "/hp":
        print ("Current HP: \t" + str(HP))
    elif input[0] == "/inv":
        pass
    elif input[0] == "/time":
        print ("The Current time is: " + str(time.time() - start_time))
        game_time()

    elif input[0] == "/info":   # Done
        print (room_list[current_room][0])

    else:
        print("That is not a valid input, type /help for a list of commands")

def input_parser(input):
    global current_room, room_list

    if input == 'n' or input == 'north':
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
        else:
            current_room = next_room
            display_description(current_room)

    elif input == 'e' or input == 'east':
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
        else:
            current_room = next_room
            display_description(current_room)

    elif input == 's' or input == 'south':
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
        else:
            current_room = next_room
            display_description(current_room)

    elif input == 'w' or input == 'west':
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
        else:
            current_room = next_room
            display_description(current_room)
    else:
        commands(input)