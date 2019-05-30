from helpers import clear_screen
from time import sleep

from item import Item


class Player:
    """An object to represent the Player

    Args:
        name: String -- The name of the Player
        current_room: String -- the current Room the player is in
        [inventory]: List -- The items a player is holding
    """

    def __init__(self, name: str, current_room: str, inventory: list = None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def list_inventory(self):
        if self.inventory is None:
            clear_screen()
            print(f"{self.name} isn't carrying anything")
            sleep(1)
            return

        clear_screen()
        print(f"{self.name}'s current inventory:")
        for item in self.inventory:
            print(f"\t* {item}")

    def get_item(self, item_name):
        if self.inventory is None:
            self.inventory = []

        # get the list of items in the room
        room_items = self.current_room.inventory

        # Return a message if the item doesn't exist
        if len(room_items) < 1:
            print(f"There don't appear to be any items in {self.current_room}")
            return

        item = list(filter(lambda i: i.name == item_name, room_items))[0]

        if not isinstance(item, Item):
            print("It doesn't look like you can pick that up")
            return

        self.current_room.inventory.remove(item)
        self.inventory.append(item)
        clear_screen()
        item.on_take()

