# Implement a class to hold room information. This should have name and
# description attributes.


# n_to`, `s_to`, `e_to`, and `w_to

class Room:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
        

    def __str__(self):
        return f"{self.room_name}. {self.description}"
        # Directions: N: {self.n_to}, S: {self.s_to}, E: {self.e_to}, W: {self.w_to}"
  