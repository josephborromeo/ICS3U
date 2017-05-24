import time, random, sys
from Rooms import *

# Define Game Variables
player_name = input("Hello Adventurer! What is your name: ")

# In game time
start_time = time.time() - 720

# Starting HP
HP = 10

# Starting Attack Damage
attack = 2

# Starting counter attack - low % to make it fair
counter_attack = 0.35

# Define player's weapons
weapon = "Fists"

# Starting inventory Space
max_inventory = 2

# Need to implement library challenge - DONE

# Need to implement usage of player name

def secret_access():
    if current_room == 14:
        pass
    else:
        pass

def eat():
    global HP
    if player_inventory[2] > 0:
        player_inventory[2] -= 1
        HP += 1
        print("HP +1")
    else:
        print("You have no food to eat")

def unlock_prompt():
    global current_room, next_room
    if next_room in key_rooms:
        if player_inventory[0] > 0:
            choice = input("Would you like to use a Key on this room? (Y or N): ")
            choice = choice.lower()
            if choice == 'y' or choice == 'yes':
                player_inventory[0] -= 1
                room_list[next_room][6] = False # Set locked flag to false
                current_room = next_room
                check_for_enemies()
                display_description(current_room)
            elif choice == 'n' or choice == 'no':
                pass
            else:
                print("That is not a valid input")
        else:
            print ("Find a key to unlock this room")
    elif next_room in key_card_rooms and next_room != 15:
        if player_inventory[1] > 0:
            choice = input("Would you like to use a Key Card on this room? (Y or N): ")
            choice = choice.lower()
            if choice == 'y' or choice == 'yes':
                player_inventory[1] -= 1
                room_list[next_room][6] = False  # Set locked flag to false
                current_room = next_room
                check_for_enemies()
                display_description(current_room)
            elif choice == 'n' or choice == 'no':
                pass
            else:
                print("That is not a valid input")
        else:
            print("Find a Key Card to unlock this room")
    elif (current_room == 11 and next_room == 21) or (current_room == 2 and room_list[11][6] is False):
        room_list[next_room][6] = False  # Set locked flag to false
        current_room = next_room
        check_for_enemies()
        display_description(current_room)
    elif current_room == 14 and next_room == 15:
        current_time = time.time() - start_time
        hour = int(current_time // 60)
        if hour >= 24:
            hour = hour - ((hour // 24) * 24)
            if hour > 10 and hour < 23:
                if player_inventory[1] > 0:
                    choice = input("Would you like to use a Key Card on this room? (Y or N): ")
                    choice = choice.lower()
                    if choice == 'y' or choice == 'yes':
                        player_inventory[1] -= 1
                        room_list[next_room][6] = False  # Set locked flag to false
                        current_room = next_room
                        check_for_enemies()
                        display_description(current_room)
                    elif choice == 'n' or choice == 'no':
                        pass
                    else:
                        print("That is not a valid input")
                else:
                    print("Find a Key Card to unlock this room")
            else:
                print("It's not time for that...")
        else:
            if hour > 10 and hour < 23:
                if player_inventory[1] > 0:
                    choice = input("Would you like to use a Key Card on this room? (Y or N): ")
                    choice = choice.lower()
                    if choice == 'y' or choice == 'yes':
                        player_inventory[1] -= 1
                        room_list[next_room][6] = False  # Set locked flag to false
                        current_room = next_room
                        check_for_enemies()
                        display_description(current_room)
                    elif choice == 'n' or choice == 'no':
                        pass
                    else:
                        print("That is not a valid input")
                else:
                    print("Find a Key Card to unlock this room")
            else:
                print("It's not time for that...")


    else:
        pass

def key_check():
    global key_flag
    key_flag = False
    for i in room_list[current_room][7]:
        if i == 'key':
            key_flag = True
        else:
            pass

def key_card_check():
    global key_card_flag
    key_card_flag = False
    for i in room_list[current_room][7]:
        if i == 'key_card':
            key_card_flag = True
        else:
            pass

#       WORKING
def take_items(input):
    global max_inventory, player_inventory
    key_card_check()
    key_check()
    if len(input) == 1 or (len(input) == 2 and input[1]==''):
        print ('Invalid Paramaters: Specify an item to take')
    else:
        if inventory_count() < max_inventory:
            if len(input) == 2 and input[1] == 'key' and key_flag == True:
                room_list[current_room][7].remove('key')
                player_inventory[0]+=1
                print("Key added to inventory!")
            elif input[1] == 'bag' and room_list[current_room][7].count('bag'):
                room_list[current_room][7].remove('bag')
                max_inventory += 5
                print("Inventory space increased!")
            elif input[1] == 'food' and room_list[current_room][7].count('food'):
                room_list[current_room][7].remove('food')
                player_inventory[2]+=1
                print("Food added to inventory!")
            elif input[1] == 'weapon' and room_list[current_room][7].count('weapon'):
                room_list[current_room][7].remove('weapon')
                weapon_chooser()
            elif len(input) > 2:
                if (input[1] == 'key' and input[2] == 'card') and key_card_flag == True:
                    room_list[current_room][7].remove('key_card')
                    player_inventory[1]+=1
                    print("Key Card added to inventory!")
                else:
                    print("That item is not here")
            else:
                print("That item is not here")
        else:
            if len(room_list[current_room][7]) == 0 or room_list[current_room][7][0] is None:
                print("That item is not here")
            else:
                print("Sorry, your inventory is too full")

# Counts how many items the player is currently holding - WORKING
def inventory_count():
    global player_inventory
    inventory_amount = 0
    for i in player_inventory:
        inventory_amount += i
    return inventory_amount

#           WORKING
def display_inventory():
    print("# of Keys: " + str(player_inventory[0]))
    print("# of Key Cards: " + str(player_inventory[1]))
    print("# of Food: " + str(player_inventory[2]))

# Working
def game_time():
    current_time = time.time() - start_time
    hour = int(current_time // 60)
    mins = int(current_time - hour*60)
    if hour >= 24:
        hour = hour- ((hour//24)*24)
    if hour >= 0 and hour < 12:
        print("The Current time is: " + str(hour) + ":" + str(mins).zfill(2) + " am")
    elif hour == 12:
        print ("The Current time is: " + str(hour) + ":" + str(mins).zfill(2) + " pm")
    elif hour > 12 and hour < 24:
        print("The Current time is: " + str(hour-12) + ":" + str(mins).zfill(2) + " pm")

# Working
def display_items():
    if len(room_list[current_room][7]) > 0:
        if room_list[current_room][7][0] is None:
            print (found_none[random.randint(0,len(found_none)-1)])
        else:
            print("Found\n------")
            for i in room_list[current_room][7]:
                if i == 'key':
                    print ("Key")
                elif i == 'bag':
                    print ('Bag')
                elif i == 'food':
                    print ('Food')
                elif i == 'key_card':
                    print ('Key Card')
                elif i == 'weapon':
                    print ('Weapon')
                else:
                    print ('Something goofed, contact developer')
    else:
        print(found_none[random.randint(0, len(found_none) - 1)])

# Working
def enemy_encounter():
    global HP
    room_list[current_room][8] = False
    # Determine enemy HP based off of player location
    if current_room == 9 or current_room == 10:
        enemy_health = 4
        enemy_attack = 1
    elif current_room == 3 or current_room == 16:
        enemy_health = random.randint(6, 10)
        enemy_attack = 3
    else:
        enemy_health = random.randint(10, 15)
        enemy_attack = 5

    # Fight Sequence - WORKING
    print ("OH NO! You encounter an enemy")
    print ('Enemy HP: ' + str(enemy_health))
    print ('Your HP: ' + str(HP) + "\tYour Attack: " + str(attack))
    while enemy_health > 0 and HP > 0:
        fight_choice = input('Choose to aim for the Body(90% chance)\nor the Head(30% chance and +2 dmg): ')
        fight_choice.lower()
        if fight_choice == 'head':
            hit = random.random() <= 0.3
            if hit is True:
                enemy_health -= (attack + 2)
                print('\nHit succesful! You did ' + str(attack + 2) + " damage")
                if enemy_health > 0:
                    print('Enemy HP: ' + str(enemy_health))
                    print('Your HP: ' + str(HP))
                    time.sleep(0.5)
                    if random.random() < counter_attack:
                        HP -= enemy_attack
                        print("\nThe enemy counter attacks and you take " + str(enemy_attack) + " damage")
                        print('Enemy HP: ' + str(enemy_health))
                        print('Your HP: ' + str(HP))
                    else:
                        pass
                else:
                    print('Enemy HP: 0')
                    print('Your HP: ' + str(HP))
            else:
                HP -= enemy_attack
                print ("\nOh no! You missed!")
                print ("The enemy hits you and you take " + str(enemy_attack) + " damage")
                print('Enemy HP: ' + str(enemy_health))
                print('Your HP: ' + str(HP))
        elif fight_choice == 'body':
            hit = random.random() <= 0.9
            if hit is True:
                enemy_health -= attack
                print('\nHit succesful! You did ' + str(attack) + " damage")
                if enemy_health > 0:
                    print('Enemy HP: ' + str(enemy_health))
                    print('Your HP: ' + str(HP))
                    time.sleep(0.5)
                    if random.random() < counter_attack:
                        HP -= enemy_attack
                        print("\nThe enemy counter attacks and you take " + str(enemy_attack) + " damage")
                        print('Enemy HP: ' + str(enemy_health))
                        print('Your HP: ' + str(HP))
                    else:
                        pass
                else:
                    print('Enemy HP: 0')
                    print('Your HP: ' + str(HP))
            else:
                HP -= enemy_attack
                print ("Oh no! You missed!")
                print ("The enemy hits you and you take " + str(enemy_attack) + " damage")
                print('Enemy HP: ' + str(enemy_health))
                print('Your HP: ' + str(HP))
        else:
            print("That is not a valid choice")
    if HP > 0:
        print("Congratulations! You have defeated the enemy, continue on!\n")
        time.sleep(2)
    else:
        print("YOU HAVE DIED")
        time.sleep(2)
        input("Press enter to exit")
        sys.exit() # Replace this with restart?

# Working
def check_for_enemies():
    if room_list[current_room][8] == False:
        pass
    else:
        enemy_encounter()


# Working
def weapon_chooser():
    '''Gun or Sword
        Gun - +2 damage, only 20% chance of being hit by a counter attack
        Sword = +4 damage, 50% chance of being hit by a counter attack'''
    global attack, counter_attack, weapon
    if current_room == 11:
        print("Choose your weapon"
              "\nGun - +2 Attack Damage, 20% chance of enemy counter attack"
              "\nSword - +4 Attack Damage, 50% chance of enemy counter attack")
        while attack == 2:
            weapon = input("To choose type 'gun' or 'sword': ")
            weapon = weapon.lower()
            if weapon == 'gun':
                attack += 2
                counter_attack = 0.2
                weapon = "Gun"
            elif weapon == 'sword':
                attack += 4
                counter_attack = 0.5
                weapon = "Sword"
    elif current_room == 16:
        attack += 5
        counter_attack = 0.75
        weapon = "Plasma Rifle"
        print("You pick up a plasma rifle from the lab"
              "\nYou gain +5 Attack with a 25% chance of an enemy counter attack")
        input("Press any key to continue")
    else:
        print("There shouldn't be a weapon here")

# Working
def split_desc(room):
    decription = room_list[current_room][0].split('\n')
    print(decription[0] + '\n' + decription[-1])

# Working
def display_description(room):
    if room_list[current_room][5] == False:
        print (room_list[current_room][0])
        room_list[current_room][5] = True
    else:
        split_desc(room)

def commands(input):
    '''
    Displays Commands when the user types them in
    All commands: /help, /search, /hp, /inv, /time, /take, /info, /stats, /eat
    :param input: 
    :return: 
    '''
    input = input.split(" ")
    # Help Command
    if (input[0] == "/help" and len(input) == 1 ) or (input[0] == "/?" and len(input) == 1):
        print("\t\t\t\tCommands\n----------------------------------------------------------"
              "\n/help\t\tPrints help dialog"
              "\n/search\t\tSearches the room for entities"
              "\n/hp\t\tDisplays your current and max HP"
              "\n/inv\t\tDisplays your current and max inventory"
              "\n/time\t\tDisplays the current in game time"
              "\n/take item\tAdds the corresponding item to your inventory"
              "\n/info\t\tDisplays information about the current room"
              "\n/stats\t\tDisplays current player stats"
              "\n/eat\t\tConsumes 1 food item to gain 1 HP")
    # Search Command
    elif input[0] == "/search" and len(input) == 1:
        print("Searching Room...\n")
        time.sleep(0.5)
        display_items()

    elif input[0] == "/hp" and len(input) == 1:
        print ("Current HP: \t" + str(HP))

    elif input[0] == "/inv" and len(input) == 1:
        display_inventory()

    elif input[0] == "/time" and len(input) == 1:
        print ("The Current time is: " + str(time.time() - start_time))
        game_time()

    elif input[0] == "/take":
        take_items(input)

    elif input[0] == "/stats" and len(input) == 1:
        print("Current HP: \t " + str(HP))
        print("Current Attack:  " + str(attack))
        print("Current Weapon:  " + weapon)
        print("Inventory Space: " + str(inventory_count()) + '/' + str(max_inventory) + ' slots used')
        print("%.2f Minutes Played"%(((time.time()-start_time)/60)-12))

    elif input[0] == "/info":   # Done
        print (room_list[current_room][0])

    elif input[0] == "/eat":
        eat()

    else:
        print("That is not a valid input, type /help for a list of commands")

def input_parser(input):
    global current_room, room_list, next_room

    if input == 'n' or input == 'north':
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)

    elif input == 'e' or input == 'east':
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)

    elif input == 's' or input == 'south':
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)

    elif input == 'w' or input == 'west':
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        elif room_list[next_room][6] == True:
            print ("Sorry that room is locked!")
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)
    else:
        commands(input)