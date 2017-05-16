import time

room_list = [["Center Starting Room", None, 6, 1, 14],
             ["Hallway 1", 0, None, 2, None],
             ["Cell Hall 1", 1, 21, 3, None],
             ["Cell Hall 2", 2, 4, None, 5],
             ["Men's Bathroom", None, None, None, 3],
             ["Women's Bathroom", None, 3, None, None],
             ["Long Corridor Part 1", None, 7, 22, 0],
             ["Long Corridor Part 2", 12, 8, None, 6],
             ["Long Corridor Part 3", None, 9, None, 7],
             ["Storage Room", 10, None, 11, None],
             ["Electrical Room", None, None, 9, None],
             ["Weaponry", 9, None, None, 21],
             ["Medical Room", None, None, 7, 13],
             ["Employee Room", None, 12, None, None],
             ["Library", 17, 0, 15, None],
             ["Secret Library Corridor", 14, None, 16, None],
             ["Secret Lab", 15, None, None, None],
             ["Outside Courtyard", 18, None, 14, None],
             ["Security/ Surveillance Office", None, 19, 17, None],
             ["Head Office", None, 20, None, 18],
             ["Escape", None, 20, None, 19],
             ["Kitchen", 6, None, None, None]]


current_room = 0
done = False

print(room_list[current_room][0])

while not done:
    direction = input("What direction would you like to go in - N, S, E, W?")
    direction = direction.lower()
    if direction == 'n' or direction == 'north':
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    elif direction == 'e' or direction == 'east':
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    elif direction == 's' or direction == 'south':
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    elif direction == 'w' or direction == 'west':
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print(room_list[current_room][0])
    else:
        print("That is not a valid direction")
