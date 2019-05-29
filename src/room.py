class Room:
    """The room class contains a constructor to instanciate a new room.
    The room contains a method to print it's description. Trigger the
    method on this room when a player enters"""

    def __init__(self, name, description, inventory=None):
        self.name = name
        self.description = description
        self.inventory = inventory
