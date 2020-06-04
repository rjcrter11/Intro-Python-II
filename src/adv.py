from room import Room
from player import Player
from item import Item
import textwrap
from bcolors import bcolors
from textwrap import dedent, indent


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
grab one of the torches before you head to through the door  to the west"""),

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


# Text wrapping for better line breaks

def wrapper(text):
    wrapped = textwrap.fill(textwrap.dedent(
        text), width=50, initial_indent=" ", subsequent_indent=" ")
    return wrapped

# Item description strings to feed to wrapper function


item_desc1 = "Use the pointy end."
item_desc2 = "Ooh, she thicc"
item_desc3 = "Let's not pretend. You can't pull that string all the way back"
item_desc4 = "Score. Who left this tasty DP here? It ain't even flat. Maybe this was the real treasure all along"
item_desc5 = "This should help you see in the dark"


# Declare Items

items = {
    "sword": Item("Sword", wrapper(item_desc1)),
    "shield": Item("Shield", wrapper(item_desc2)),
    "bow": Item("Bow", wrapper(item_desc3)),
    "soda": Item("Soda", wrapper(item_desc4)),
    'torch': Item("Torch", wrapper(item_desc5))
}

# Add items to rooms

room['foyer'].items.append(items['sword'])
room['overlook'].items.append(items['shield'])
room['narrow'].items.append(items['bow'])
room['treasure'].items.append(items['soda'])
room['hallway'].items.append(items['torch'])

# Opening message for directions

ded_text = textwrap.dedent(
    "To make your way through the maze, choose a direction: North[n], East[e], South[s], or West[w].")
ded_text2 = textwrap.dedent(
    "To pick up an item, use [get] or [pickup]. To drop it, use [drop] or [leave]. To check your inventory, type [bag]")
ded_text3 = textwrap.dedent("To quit, press [q]")
ded_text4 = textwrap.dedent("For help, type [help]")


def prompt(message):
    print(f"\n{bcolors.OKGREEN}***************************************************************{bcolors.ENDC}\n")
    print(f"{message} \n")
    print(textwrap.fill(ded_text, width=60))
    print(textwrap.fill(ded_text2))
    print(textwrap.fill(ded_text3))
    print(textwrap.fill(ded_text4))
    print("Good Luck!")
    print(f"\n{bcolors.OKGREEN}***************************************************************{bcolors.ENDC}\n\n")


# Make a new player object that is currently in the 'outside' room.
new_player_name = input(f"\nEnter player name: ")
player = Player(new_player_name, room["outside"])

prompt(f"{bcolors.HEADER}Welcome {player.name}!{bcolors.ENDC}")
#is_dark = True

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

# Takes current room name and description for printing


def current_room(arg):
    dedented_text = textwrap.dedent(f"{arg.current_room.description} ")
    print(
        f"\n{bcolors.OKBLUE}================================================={bcolors.ENDC}")
    print(f"\n {bcolors.BOLD}  -{arg.current_room.name}- {bcolors.ENDC}")
    print(dedented_text)
    player.current_room.item_check()
    arg.check_torch()
    print(f"\n{bcolors.OKBLUE}================================================={bcolors.ENDC}\n")


command = ""
while command != "q":
    current_room(player)
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
            print(
                f"{bcolors.HEADER}============================================={bcolors.ENDC}\n")
            print(textwrap.fill(textwrap.dedent(
                f"\n{bcolors.BOLD}Ah, the real treasure was inside you this whole time.{bcolors.ENDC}"), width=50, subsequent_indent=" "))
            print(f"\n{bcolors.BOLD}              Buh bye now.")
            print(
                f"\n{bcolors.HEADER}============================================={bcolors.ENDC}")
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
