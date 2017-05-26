import time, random, sys
from Rooms import *

# Define Game Variables

# Player Name
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

# Function to print words out letter by letter
def text_typer(string, delay):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)

# End game sequence when the player escapes - Closes the program
def end_game():
    global done
    done = True
    text_typer("\n\nYou open the door to the outside and are blinded by light of the shining sun\n", 0.05)
    time.sleep(0.4)
    text_typer("You step out and find a knife on the ground, you use it to carve " + player_name + " into the back side of the door\n", 0.045)
    text_typer("You did it, you beat the prison. You start walking to the closest road hoping to find some help...\n\n", 0.07)
    time.sleep(1)
    text_typer("CONGRATULATIONS! YOU BEAT THE GAME!\n", 0.04)
    input("Press Enter to exit")
    sys.exit()

# Command to remove a food item from inventory and add 1 HP to the player's health
def eat():
    global HP
    if player_inventory[2] > 0:
        player_inventory[2] -= 1
        HP += 1
        text_typer("HP +1", 0.02)
    else:
        text_typer("You have no food to eat", 0.02)


# Asks the user if they would like to unlock the locked room they are trying to access
def unlock_prompt():
    global current_room, next_room
    if next_room in key_rooms:
        if player_inventory[0] > 0:
            choice = input("Would you like to use a Key on this room? (Y or N): ")
            choice = choice.lower()
            if choice == 'y' or choice == 'yes':
                if next_room == 11:
                    player_inventory[0] -= 1
                    room_list[21][6] = False
                    room_list[next_room][6] = False # Set locked flag to false
                    current_room = next_room
                    check_for_enemies()
                    display_description(current_room)
                else:
                    player_inventory[0] -= 1
                    room_list[next_room][6] = False  # Set locked flag to false
                    current_room = next_room
                    check_for_enemies()
                    display_description(current_room)
            elif choice == 'n' or choice == 'no':
                pass
            else:
                text_typer("That is not a valid input", 0.03)
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
                text_typer("That is not a valid input", 0.03)
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
                        text_typer("That is not a valid input", 0.03)
                else:
                    text_typer("Find a Key Card to unlock this room", 0.03)
            else:
                text_typer("It's not time for that...", 0.03)
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
                        text_typer("That is not a valid input", 0.03)
                else:
                    text_typer("Find a Key Card to unlock this room", 0.03)
            else:
                text_typer("It's not time for that...", 0.03)
    else:
        pass

# Checks if there is a Key in the current room
def key_check():
    global key_flag
    key_flag = False
    for i in room_list[current_room][7]:
        if i == 'key':
            key_flag = True
        else:
             pass

# Checks if there is a Key Card in the current room
def key_card_check():
    global key_card_flag
    key_card_flag = False
    for i in room_list[current_room][7]:
        if i == 'key_card':
            key_card_flag = True
        else:
            pass

# Command to take items from the current room and add them to the player's inventory
def take_items(input):
    global max_inventory, player_inventory
    key_card_check()
    key_check()
    if len(input) == 1 or (len(input) == 2 and input[1]==''):
        text_typer('Invalid Paramaters: Specify an item to take\n', 0.03)
    else:
        if inventory_count() < max_inventory:
            if len(input) == 2 and input[1] == 'key' and key_flag == True:
                room_list[current_room][7].remove('key')
                player_inventory[0]+=1
                text_typer("Key added to inventory!\n", 0.03)
            elif input[1] == 'bag' and room_list[current_room][7].count('bag'):
                room_list[current_room][7].remove('bag')
                max_inventory += 5
                text_typer("Inventory space increased!\n", 0.03)
            elif input[1] == 'food' and room_list[current_room][7].count('food'):
                room_list[current_room][7].remove('food')
                player_inventory[2]+=1
                text_typer("Food added to inventory!\n", 0.03)
            elif input[1] == 'weapon' and room_list[current_room][7].count('weapon'):
                room_list[current_room][7].remove('weapon')
                weapon_chooser()
            elif len(input) > 2:
                if (input[1] == 'key' and input[2] == 'card') and key_card_flag == True:
                    room_list[current_room][7].remove('key_card')
                    player_inventory[1]+=1
                    text_typer("Key Card added to inventory!\n", 0.03)
                else:
                    text_typer("That item is not here\n", 0.03)
            else:
                text_typer("That item is not here\n", 0.03)
        else:
            if len(room_list[current_room][7]) == 0 or room_list[current_room][7][0] is None:
                text_typer("That item is not here\n", 0.03)
            else:
                text_typer("Sorry, your inventory is too full\n", 0.03)

# Counts how many items the player is currently holding
def inventory_count():
    global player_inventory
    inventory_amount = 0
    for i in player_inventory:
        inventory_amount += i
    return inventory_amount

# Command to print the player's current inventory
def display_inventory():
    print("# of Keys: " + str(player_inventory[0]))
    print("# of Key Cards: " + str(player_inventory[1]))
    print("# of Food: " + str(player_inventory[2]))

# Displays the ingame time
def game_time():
    current_time = time.time() - start_time
    hour = int(current_time // 60)
    mins = int(current_time - hour*60)
    if hour >= 24:
        hour = hour- ((hour//24)*24)
    if hour >= 0 and hour < 12:
        text_typer("The Current time is: " + str(hour) + ":" + str(mins).zfill(2) + " am", 0.05)
    elif hour == 12:
        text_typer ("The Current time is: " + str(hour) + ":" + str(mins).zfill(2) + " pm", 0.05)
    elif hour > 12 and hour < 24:
        text_typer("The Current time is: " + str(hour-12) + ":" + str(mins).zfill(2) + " pm", 0.05)

# Displays the items in the current room
def display_items():
    if len(room_list[current_room][7]) > 0:
        if room_list[current_room][7][0] is None:
            text_typer(found_none[random.randint(0,len(found_none)-1)] + '\n', 0.03)
        else:
            text_typer("Found\n------\n", 0.03)
            for i in room_list[current_room][7]:
                if i == 'key':
                    text_typer ("Key\n", 0.03)
                elif i == 'bag':
                    text_typer ('Bag\n', 0.03)
                elif i == 'food':
                    text_typer ('Food\n', 0.03)
                elif i == 'key_card':
                    text_typer ('Key Card\n', 0.03)
                elif i == 'weapon':
                    text_typer ('Weapon\n', 0.03)
                else:
                    print ('Something goofed, contact developer')
    else:
        text_typer(found_none[random.randint(0, len(found_none) - 1)] + '\n', 0.03)

# Enemy fight sequence if there is an enemy in the current room
def enemy_encounter():
    global HP
    room_list[current_room][8] = False
    # Determine enemy HP based off of player location
    if current_room == 9 or current_room == 10:
        enemy_health = 4
        enemy_attack = 1
    elif current_room == 3 or current_room == 16:
        enemy_health = random.randint(6, 8)
        enemy_attack = 3
    else:
        enemy_health = random.randint(10, 14)
        enemy_attack = 4

    # Fight Sequence - WORKING
    text_typer("OH NO! You encounter an enemy\n", 0.06)
    text_typer('Enemy HP: ' + str(enemy_health) + '\n', 0.05)
    text_typer('Your HP: ' + str(HP) + "\tYour Attack: " + str(attack) + '\n', 0.05)
    while enemy_health > 0 and HP > 0:
        fight_choice = input('Choose to aim for the Body(90% chance)\nor the Head(30% chance and +2 dmg): ')
        fight_choice.lower()
        if fight_choice == 'head':
            hit = random.random() <= 0.3
            if hit is True:
                enemy_health -= (attack + 2)
                text_typer('\nHit succesful! You did ' + str(attack + 2) + " damage", 0.04)
                if enemy_health > 0:
                    text_typer('Enemy HP: ' + str(enemy_health) + '\n', 0.04)
                    text_typer('Your HP: ' + str(HP) + '\n', 0.04)
                    time.sleep(0.5)
                    if random.random() < counter_attack:
                        HP -= enemy_attack
                        text_typer("\nThe enemy counter attacks and you take " + str(enemy_attack) + " damage\n", 0.04)
                        text_typer('Enemy HP: ' + str(enemy_health) + '\n', 0.04)
                        text_typer('Your HP: ' + str(HP) + '\n', 0.04)
                    else:
                        pass
                else:
                    text_typer('Enemy HP: 0\n', 0.04)
                    text_typer('Your HP: ' + str(HP) + '\n', 0.04)
            else:
                HP -= enemy_attack
                text_typer("\nOh no! You missed!\n", 0.04)
                text_typer("The enemy hits you and you take " + str(enemy_attack) + " damage\n", 0.04)
                text_typer('Enemy HP: ' + str(enemy_health) + '\n', 0.04)
                text_typer('Your HP: ' + str(HP) + '\n', 0.04)
        elif fight_choice == 'body':
            hit = random.random() <= 0.9
            if hit is True:
                enemy_health -= attack
                text_typer('\nHit succesful! You did ' + str(attack) + " damage\n", 0.04)
                if enemy_health > 0:
                    text_typer('Enemy HP: ' + str(enemy_health) + '\n', 0.04)
                    text_typer('Your HP: ' + str(HP) + '\n', 0.04)
                    time.sleep(0.5)
                    if random.random() < counter_attack:
                        HP -= enemy_attack
                        text_typer("\nThe enemy counter attacks and you take " + str(enemy_attack) + " damage\n", 0.04)
                        text_typer('Enemy HP: ' + str(enemy_health) + '\n', 0.04)
                        text_typer('Your HP: ' + str(HP) + '\n', 0.04)
                    else:
                        pass
                else:
                    text_typer('Enemy HP: 0\n', 0.04)
                    text_typer('Your HP: ' + str(HP) + '\n', 0.04)
            else:
                HP -= enemy_attack
                text_typer("Oh no! You missed!\n", 0.04)
                text_typer("The enemy hits you and you take " + str(enemy_attack) + " damage\n", 0.04)
                text_typer('Enemy HP: ' + str(enemy_health) + '\n', 0.04)
                text_typer('Your HP: ' + str(HP) + '\n', 0.04)
        else:
            text_typer("That is not a valid choice\n", 0.04)
    if HP > 0:
        text_typer("Congratulations! You have defeated the enemy, continue on!\n", 0.04)
        time.sleep(1)
    else:
        text_typer("YOU HAVE DIED\n", 0.1)
        time.sleep(2)
        input("Press enter to exit")
        sys.exit() # Replace this with restart?

# Checks for enemies for the current room
def check_for_enemies():
    if room_list[current_room][8] == False:
        pass
    else:
        enemy_encounter()


# Command for the player to choose what weapon they want
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
        text_typer("You pick up a plasma rifle from the lab"
              "\nYou gain +5 Attack with a 25% chance of an enemy counter attack\n", 0.06)
        input("Press any key to continue")
    else:
        print("There shouldn't be a weapon here")

# Command to shorten the discription of rooms to only the title and possible directions
def split_desc(room):
    decription = room_list[current_room][0].split('\n')
    print(decription[0] + '\n' + decription[-1])

# Prints the current room's description
def display_description(room):
    if room_list[current_room][5] == False:
        print (room_list[current_room][0])
        room_list[current_room][5] = True
    else:
        split_desc(room)

# Command that handles all user input that is not a movement command
def commands(input):
    '''
    Displays Commands when the user types them in
    All commands: /help, /search, /hp, /inv, /time, /take, /info, /stats, /eat
    '''
    input = input.split(" ")
    # Help Command
    if (input[0] == "/help" and len(input) == 1 ) or (input[0] == "/?" and len(input) == 1):
        print("\t\t\t\tCommands\n----------------------------------------------------------"
              "\nN\t\tMoves to the North"
              "\nS\t\tMoves to the South"
              "\nE\t\tMoves to the East"
              "\nW\t\tMoves to the West"
              "\n/help\t\tPrints help dialog"
              "\n/search\t\tSearches the room for entities"
              "\n/hp\t\tDisplays your current and max HP"
              "\n/inv\t\tDisplays your current and max inventory"
              "\n/time\t\tDisplays the current in game time"
              "\n/take <item>\tAdds the corresponding item to your inventory"
              "\n/info\t\tDisplays information about the current room"
              "\n/stats\t\tDisplays current player stats"
              "\n/eat\t\tConsumes 1 food item to gain 1 HP")
    # Search Command
    elif input[0] == "/search" and len(input) == 1:
        text_typer("Searching Room...\n", 0.03)
        time.sleep(0.2)
        display_items()

    elif input[0] == "/hp" and len(input) == 1:
        text_typer("Current HP: \t" + str(HP) + '\n', 0.03)

    elif input[0] == "/inv" and len(input) == 1:
        display_inventory()

    elif input[0] == "/time" and len(input) == 1:
        game_time()

    elif input[0] == "/take":
        take_items(input)

    elif input[0] == "/stats" and len(input) == 1:
        print("\nCurrent HP: \t " + str(HP))
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

# Handles all the player input and movement
def input_parser(input):
    global current_room, room_list, next_room

    if current_room == 20 and input == 'e' or input == 'east':
        end_game()

    elif input == 'n' or input == 'north':
        next_room = room_list[current_room][1]
        if next_room == None:
            text_typer("You can't go that way",0.03)
        elif room_list[next_room][6] == True:
            text_typer("Sorry that room is locked!\n", 0.03)
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)

    elif input == 'e' or input == 'east':
        next_room = room_list[current_room][2]
        if next_room == None:
            text_typer("You can't go that way\n", 0.03)
        elif room_list[next_room][6] == True:
            text_typer("Sorry that room is locked!\n", 0.03)
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)

    elif input == 's' or input == 'south':
        next_room = room_list[current_room][3]
        if next_room == None:
            text_typer("You can't go that way\n", 0.03)
        elif room_list[next_room][6] == True:
            text_typer("Sorry that room is locked!\n", 0.03)
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)

    elif input == 'w' or input == 'west':
        next_room = room_list[current_room][4]
        if next_room == None:
            text_typer("You can't go that way\n", 0.03)
        elif room_list[next_room][6] == True:
            text_typer("Sorry that room is locked!\n", 0.03)
            unlock_prompt()
        else:
            current_room = next_room
            check_for_enemies()
            display_description(current_room)
    else:
        commands(input)