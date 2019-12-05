
# Write a class to hold player information, e.g. what room they are in
# currently.
import sys
# print(sys.path)


class Player:
    def __init__(self, player_name, role, sex):
        self.player_name = player_name
        self.current_room = 'outside'
        self.role = role
        self.sex = sex
    
    def __str__(self):
        return f"{self.player_name} is {self.current_room}"


# p = Player("bob", "magician", "m")
# print(p)







