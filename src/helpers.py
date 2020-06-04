from bcolors import bcolors
import textwrap
from textwrap import dedent

# Gets current room name and description for printing


def current_room(arg):
    dedented_text = textwrap.dedent(f"{arg.current_room.description} ")
    print(text_color(
        f"\n=================================================", bcolors.OKBLUE))
    print(text_color(f"\n   -{arg.current_room.name}- ", bcolors.BOLD))
    print(dedented_text)
    arg.current_room.item_check()
    arg.check_torch()
    print(text_color(
        f"\n=================================================", bcolors.OKBLUE))


# Opening message for directions

ded_text = textwrap.dedent(
    "To make your way through the maze, choose a direction: North[n], East[e], South[s], or West[w].")
ded_text2 = textwrap.dedent(
    "To pick up an item, use [get] or [pickup]. To drop it, use [drop] or [leave]. To check your inventory, type [bag]")
ded_text3 = textwrap.dedent("To quit, press [q]")
ded_text4 = textwrap.dedent("For help, type [help]")


def prompt(message):
    print(text_color(
        f"\n***************************************************************\n", bcolors.OKGREEN))
    print(f"{message} \n")
    print(textwrap.fill(ded_text, width=60))
    print(textwrap.fill(ded_text2))
    print(textwrap.fill(ded_text3))
    print(textwrap.fill(ded_text4))
    print("Good Luck!")
    print(text_color(
        f"\n***************************************************************\n", bcolors.OKGREEN))


# Text wrapping for better line breaks

def wrap(text, initial, sub):
    wrapped = textwrap.fill(textwrap.dedent(
        text), width=50, initial_indent=initial, subsequent_indent=sub)
    return wrapped

# Quit message


def on_quit():
    print(text_color("=============================================", bcolors.HEADER))
    print(wrap(text_color(
        f"\nAh, the real treasure was inside you this whole time.", bcolors.BOLD), " ", "  "))
    print(f"\n{bcolors.BOLD}              Buh bye now.")
    print(text_color("=============================================", bcolors.HEADER))

# Text color function


def text_color(text, col):
    return f"{col}{text}{bcolors.ENDC}"
