
from player import Player
from room import Room
from item import Item

import textwrap
import random

item = {
    'torch': Item("torch", "A torch lights your path"),
    'key': Item("key", "A large rusty key"),
    'ale': Item("ale", "A goblet of ale"),
    'mutton': Item("mutton", "A juicy large leg of lamb"),
    'map': Item("map", "Old warn parchment map faintly marks the rumored treasure"),
    'sword': Item("sword", "A broad gleaming sword hidden within an unremarkable scabbard"),
    'rope': Item("rope", "50ft of thick rope"),
    'shovel': Item("shovel", "A shovel"),
    'coin': Item("coin", "A coin for your leather pouch")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", items=[item['torch']]),

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

# Link rooms to item

#Main
#

player1 = Player("Bob", "magician", "male")


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
def game(player): 
    print(f"{player.player_name} your adventure begins at the {room[player.current_room]}!")
    while True:
        cmd = str(input("[n] North  [s] South   [e] East   [w] West    [q] Quit:\n"))

        if cmd == "n":
            try:
                enter_room_n = room[player.current_room].n_to
                if player.current_room == "foyer":
                    player.current_room = "overlook"
                elif player.current_room == "outside": 
                    player.current_room = "foyer"
                elif player.current_room == "narrow":
                    player.current_room = "treasure"
                print(f"You are now in the {room[player.current_room]}")
            except AttributeError:
                 print("You must seek another direction!")
        elif cmd == "s":
            try:
                enter_room_s = room[player.current_room].s_to
                if player.current_room == "overlook":
                    player.current_room = "foyer"
                elif player.current_room == "foyer":
                    player.current_room = "outside"
                elif player.current_room == "treasure":
                    player.current_room = "narrow"
                print(f"You are now in the {room[player.current_room]}")
            except AttributeError:
                 print("You must seek another direction!")
        elif cmd == "e":
            try:
                enter_room_e = room[player.current_room].e_to
                player.current_room = "narrow"
                print(f"You are now in the {room[player.current_room]}")
            except AttributeError:
                 print("You must seek another direction!")
        elif cmd == "w":
            try:
                enter_room_w = room[player.current_room].w_to
                player.current_room = "foyer"
                print(f"You are now in the {player.current_room},  {room[player.current_room]}")
            except AttributeError:
                 print("You must seek another direction!")
        elif cmd == "q":
            print(f"Goodbye!")
            break
        else:
            str(input("Please enter a valid command: [n] North  [s] South   [e] East   [w] West    [q] Quit:\n"))


if __name__ == '__main__':
      game(player1)