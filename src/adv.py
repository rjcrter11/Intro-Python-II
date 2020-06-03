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
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


def prompt(message):
    ded_text = textwrap.dedent(
        "To make your way through the maze, choose a direction: North[n], East[e], South[s], or West[w]. To pick up an item, use [get]. To drop it, use [drop]. To quit, press [q] ")
    print("\n***************************************************************\n")
    print(f"{message}")
    print(textwrap.fill(ded_text))
    print("Good Luck!")
    print("\n***************************************************************\n\n")


# Make a new player object that is currently in the 'outside' room.
new_player_name = input("Enter player name: ")
player = Player(new_player_name, room["outside"])

prompt(
    f"Welcome {player.name}")


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


command = ""

while command != "Q":
    current_room(player)
    command = input(
        f"\n{player.name}, what will you do?: ")
    player_action = command.lower().split()
    if len(player_action) == 1:
        if command == "n" or command == 's' or command == 'e' or command == 'w':
            player.move(command)
        elif command == "q":
            print("\n Leaving so soon?")
            break
        else:
            print(" \nPlease choose a valid command\n")
