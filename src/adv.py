from room import Room
from player import Player
from item import Item
import textwrap
from bcolors import bcolors
from textwrap import dedent, indent
from helpers import current_room, prompt, wrap, on_quit, text_color


# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", False),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),

    'graveyard': Room("Dark Cemetary", """An unsettling fog hovers at your feet, and an eery glow
pulses in the distance. Maybe best to go back the way you came."""),

    'bridge': Room('Rickety Bridge', """You've found an old bridge across the chasm. The next step
may be your last. Out beyond the bridge, you must choose to head east or west."""),

    'armory': Room('The Armory', """It's full of weapons. They are covered in dust, but grabbing
 one(or a couple?) will surely make you feel safer. It looks like there's another room off to the north."""),

    'hallway': Room('Torch-lit Hallway', """The hallway is long and off-kilter. You should probably
grab one of the torches before you head to through the door  to the west""", False),

    'tunnel': Room('Pitch Black Tunnel', """The only way out is through, right? Head north
if you aren't too afraid""")

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['bridge']
room['bridge'].s_to = room['overlook']
room['bridge'].e_to = room['graveyard']
room['bridge'].w_to = room['hallway']
room['graveyard'].w_to = room['bridge']
room['hallway'].e_to = room['bridge']
room['hallway'].w_to = room['armory']
room['armory'].e_to = room['hallway']
room['armory'].n_to = room['tunnel']
room['tunnel'].s_to = room['armory']
room['tunnel'].n_to = room['treasure']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


# Item description strings to feed to wrapper function

item_desc1 = "Use the pointy end."
item_desc2 = "Ooh, she thicc"
item_desc3 = "Let's not pretend. You can't pull that string all the way back"
item_desc4 = "Score. Who left this tasty DP here? It ain't even flat. Maybe this was the real treasure all along"
item_desc5 = "This should help you see in the dark"


# Declare Items

items = {
    "sword": Item("Sword", wrap(item_desc1, " ", " ")),
    "shield": Item("Shield", wrap(item_desc2, " ", " ")),
    "bow": Item("Bow", wrap(item_desc3, " ", " ")),
    "soda": Item("Soda", wrap(item_desc4, " ", " ")),
    'torch': Item("Torch", wrap(item_desc5, " ", " "))
}

# Add items to rooms

room['foyer'].items.append(items['sword'])
room['overlook'].items.append(items['shield'])
room['narrow'].items.append(items['bow'])
room['treasure'].items.append(items['soda'])
room['hallway'].items.append(items['torch'])


# Make a new player object that is currently in the 'outside' room.
new_player_name = input(f"\nEnter player name: ")
player = Player(new_player_name, room["outside"])

prompt(text_color(f"Welcome {player.name}!", bcolors.HEADER))
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


command = ""
while command != "q":

    if player.current_room.is_dark == False:
        current_room(player)
    elif player.current_room.is_dark == True:
        if player.check_torch() == False:
            current_room(player)
        else:
            pass
    else:
        print("Its pitch dark!")
    command = input(
        f"\n{player.name}, what will you do?: ").lower().strip()
    player_action = command.split()
    if len(player_action) == 1:
        if command == "n" or command == 's' or command == 'e' or command == 'w':
            player.move(command)
        elif command == "bag":
            player.check_bag()
        elif command == 'help':
            prompt("Instructions: ")
        elif command == "q":
            on_quit()
            break
        else:
            print(" \nPlease choose a valid command\n")
    elif len(player_action) == 2:
        if player_action[0] in ['get', 'pickup']:
            if items[player_action[1]] in player.current_room.items:
                player.get(items[player_action[1]])
            else:
                print("This item is not here")
        elif player_action[0] in ['drop', 'leave']:
            if items[player_action[1]]:
                player.drop(items[player_action[1]])
            else:
                print("\n Please use a valid command\n")
        else:
            print("Please use a valid command")
    else:
        print("Error")
