from bcolors import bcolors


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"{bcolors.OKGREEN}You've picked up the {self.name}!{bcolors.ENDC}")

    def on_drop(self):
        print(f"You've dropped the {self.name}")
