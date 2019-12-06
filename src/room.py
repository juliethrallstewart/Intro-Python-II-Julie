# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, description, items =[]):
        self.room_name = room_name
        self.description = description
        self.items = items
       # self.n_to = None
        
    def __str__(self):
        return f"{self.room_name}. {self.description}"
       
    def show_items(self):
        for i in self.items:
            print(f"{i}")

    def remove_item(self, item):
        self.items.remove(item)
    
    def add_item(self, item):
        self.items.append(item)