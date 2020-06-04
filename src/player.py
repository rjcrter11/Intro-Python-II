# Write a class to hold player information, e.g. what room they are in
# currently.
from bcolors import bcolors
from helpers import text_color


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print(text_color(
                f"\n    There is no path forward in this direction.\n", bcolors.OKGREEN))

    def get(self, item):
        if len(self.current_room.items) > 0 and item not in self.items:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.on_take()
        elif item in self.items:
            print(text_color(
                f"You already have the {item.name} in your inventory", bcolors.OKGREEN))
        else:
            print(text_color("That item is not here", bcolors.OKGREEN))

    def drop(self, item):
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
            self.current_room.items.append(item)
            item.on_drop()
        else:
            print(text_color(
                f"There is no {item.name} in your inventory", bcolors.OKGREEN))

    def check_bag(self):
        if len(self.items) > 0:
            print("\n" + text_color("What's in your bag:", bcolors.OKGREEN))
            for i, item in enumerate(self.items):
                output = ""
                output += " " + str(i + 1) + ". " + item.name
                print(output)
        else:
            print(text_color("You have no items in your bag", bcolors.OKGREEN))

    def check_torch(self):

        if self.current_room.is_dark == True:
            if len(self.items) > 0:
                for item in self.items:
                    if "Torch" in item.name:
                        print(text_color(
                            "Aha! You've pulled the torch from your bag! The room explodes into light", bcolors.WARNING))
                    else:
                        print(text_color(
                            f"\nIts so dark. Sure would be good to have a torch", bcolors.HEADER))
            else:
                print(text_color(
                    f"\nIt's so dark. Sure would be good to have a torch", bcolors.HEADER))
        else:
            print(text_color(
                f"\nIt's nice and bright here. That is comforting", bcolors.WARNING))
