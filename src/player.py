class Player:
    """An object to represent the Player
    
    Args:
        name: String -- The name of the Player
        location: String -- the current Room the player is in
    """

    def __init__(self, name, location):
        self.name = name
        self.location = location
