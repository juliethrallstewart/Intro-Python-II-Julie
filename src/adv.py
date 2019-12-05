
from player import Player
from room import Room

import textwrap
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
# print(room['outside'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
#Main
#

computer = random.randint(1,3)

# if player_input == 'N':
#         if player1.CurrentRoom.n_to:
#             player1.CurrentRoom = player1.CurrentRoom.n_to
#             print(player1.CurrentRoom)
#         else:
#             print('error N')

# Make a new player object that is currently in the 'outside' room.

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
    print(f"{player.player_name} your adventure begins {room[player.current_room]}!")
    while True:
        cmd = str(input("[n] North  [s] South   [e] East   [w] West    [q] Quit:\n"))

        if cmd == "n":
            if room[player.current_room].n_to != None:
                '''print the name and description of the player's current room'''
                player.current_room = room[player.current_room].n_to
                print(f"You are now in the {player.current_room}")
            else: 
                print("You must seek another direction!")
        elif cmd == "s":
            print(f"{room[player.current_room]}")
        elif cmd == "e":
            print(f"{room[player.current_room]}")
        elif cmd == "w":
            print(f"{room[player.current_room]}")
        elif cmd == "q":
            print(f"Goodbye!")
            break
        else:
            str(input("Please enter a valid command: [n] North  [s] South   [e] East   [w] West    [q] Quit:\n"))


if __name__ == '__main__':
      game(player1)