class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __str__(self):
        return f"Item: {self.item_name}, Description: {self.item_description}"

    def __repr__(self):
        return f"Item: {self.item_name}, Description: {self.item_description}"

