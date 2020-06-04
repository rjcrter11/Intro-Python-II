# Implement a class to hold room information. This should have name and
# description attributes.
from bcolors import bcolors
from helpers import text_color


class Room:
    def __init__(self, name, description, is_dark=True):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.is_dark = is_dark

    def __str__(self):
        return f'{self.name}, {self.description} '

    def item_check(self):
        if not self.items:
            print(text_color(f"\nItems: ", bcolors.OKGREEN) +
                  "There are no useful items here\n")
        else:
            print(text_color(f"\nItems in {self.name}:", bcolors.OKGREEN))
            for item in self.items:
                print(
                    f"{item.name} {bcolors.OKGREEN}:{bcolors.ENDC} {item.description}")
