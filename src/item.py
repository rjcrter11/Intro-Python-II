from bcolors import bcolors
from helpers import text_color


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(text_color(
            f"You've picked up the {self.name}!", bcolors.OKGREEN))

    def on_drop(self):
        print(text_color(f"You've dropped the {self.name}", bcolors.OKGREEN))
