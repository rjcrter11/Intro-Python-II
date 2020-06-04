from room import Room
from player import Player
from item import Item
import textwrap
from textwrap import dedent, indent

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'graveyard': Room("Dark Cemetary", """An unsettling fog hovers at your feet, and an eery glow 
pulses in the distance. Maybe best to go back the way you came."""),

    'bridge': Room('Rickety Bridge', """You've found the bridge across the chasm. The next step 
may be your last. Out beyond the bridge, you must choose to head east or west.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['bridge']
room['bridge'].e_to = room['graveyard']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Declare Items

items = {
    "sword": Item("Sword", "Use the pointy end."),
    "shield": Item("Shield", "ooh, she thicc"),
    "bow": Item("Bow", "Let's not pretend. You can't pull that string all the way back"),
    "soda": Item("Soda", "Score. Who left this tasty DP here? It ain't even flat")
}

# Add items to rooms

room['foyer'].items.append(items['sword'])
room['overlook'].items.append(items['shield'])
room['narrow'].items.append(items['bow'])
room['treasure'].items.append(items['soda'])

# Opening message for directions

ded_text = textwrap.dedent(
    "To make your way through the maze, choose a direction: North[n], East[e], South[s], or West[w].")
ded_text2 = textwrap.dedent(
    "To pick up an item, use [get] or [pickup]. To drop it, use [drop] or [leave]. To check your inventory, type [bag]")
ded_text3 = textwrap.dedent("To quit, press [q]")
ded_text4 = textwrap.dedent("For help, type [help]")


def prompt(message):
    print("\n***************************************************************\n")
    print(f"{message} \n")
    print(textwrap.fill(ded_text, width=60))
    print(textwrap.fill(ded_text2))
    print(textwrap.fill(ded_text3))
    print(textwrap.fill(ded_text4))
    print("Good Luck!")
    print("\n***************************************************************\n\n")


# Make a new player object that is currently in the 'outside' room.
new_player_name = input("Enter player name: ")
player = Player(new_player_name, room["outside"])

prompt(f"Welcome {player.name}")


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


def current_room(arg):
    dedented_text = textwrap.dedent(f"{arg.current_room.description} ")
    print("\n=================================================")
    print(f"\n  -{arg.current_room.name}- ")
    print(dedented_text)
    print("\n=================================================\n")


command = ""
while command != "q":
    current_room(player)
    command = input(
        f"\n{player.name}, what will you do?: ").lower()
    player_action = command.split()
    if len(player_action) == 1:
        if command == "n" or command == 's' or command == 'e' or command == 'w':
            player.move(command)
            player.current_room.item_check()
        elif command == "bag":
            player.check_bag()
        elif command == 'help':
            prompt("Instructions: ")
        elif command == "q":
            print("\n Leaving so soon?")
            break
        else:
            print(" \nPlease choose a valid command\n")
    elif len(player_action) == 2:
        if player_action[0] in ['get', 'pickup']:
            if items[player_action[1]] in player.current_room.items:
                player.get(items[player_action[1]])
            else:
                print("This item is not here")
        if player_action[0] in ['drop', 'leave']:
            if items[player_action[1]]:
                player.drop(items[player_action[1]])
            else:
                print("\n Please use a valid command\n")
