
# Write a class to hold player information, e.g. what room they are in
# currently.
import sys
# print(sys.path)


class Player:
    def __init__(self, player_name, role, sex, inventory=[]):
        self.player_name = player_name
        self.current_room = 'outside'
        self.role = role
        self.sex = sex
        self.inventory = inventory
    
    def __str__(self):
        return f"{self.player_name} is {self.current_room}"

    def get_inventory(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        self.inventory.remove(item)

    def show_inventory(self):
        return f"Inventory: {self.inventory}"


# p = Player("bob", "magician", "m")
# print(p)







