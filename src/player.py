# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("\n    There is no path forward in this direction.\n")

    def get(self, item):
        if len(self.current_room.items) > 0 and item not in self.items:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.on_take()
        elif item in self.items:
            print(f"You already have the {item.name} in your inventory")
        else:
            print("Please use a valid command")

    def drop(self, item):
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
            self.current_room.items.append(item)
            item.on_drop()
        else:
            print(f"There is no {item.name} in your inventory")

    def check_bag(self):
        if len(self.items) > 0:
            print("\nWhat's in your bag: ")
            for i, item in enumerate(self.items):
                output = ""
                output += " " + str(i + 1) + ". " + item.name
                print(output)
        else:
            print("You have no items in your bag")
