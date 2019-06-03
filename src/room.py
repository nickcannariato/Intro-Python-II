class Room:
    """A geographical area in the game.

    Args:
        name: String -- the name of the location
        description: String -- a description for the location
        [inventory]: List -- the items found in the room
    """

    def __init__(self, name, description, inventory=None):
        self.name = name
        self.description = description
        self.inventory = inventory

    def __str__(self):
        """The string representation of a room"""
        return f"{self.name}\n{self.description}"
