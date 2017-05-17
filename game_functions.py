from Rooms import *

def input_parser(input):
    global current_room, room_list
    if input == 'n' or input == 'north':
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print (current_room)
            print(room_list[current_room][0])
    elif input == 'e' or input == 'east':
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(current_room)
            print(room_list[current_room][0])
    elif input == 's' or input == 'south':
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(current_room)
            print(room_list[current_room][0])
    elif input == 'w' or input == 'west':
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(current_room)
            print(room_list[current_room][0])
    else:
        print("That is not a valid input")