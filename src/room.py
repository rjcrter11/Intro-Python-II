# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f'{self.name}, {self.description} '

    def item_check(self):
        if not self.items:
            return "There are no useful items here"
        else:
            print(f"\n{self.name} has: ")
            for item in self.items:
                print(f"{item.name}")
                print(f"{item.description}")
