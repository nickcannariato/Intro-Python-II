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

