class Player:
    """An object to represent the Player
    
    Args:
        name: String -- The name of the Player
        current_room: String -- the current Room the player is in
    """

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
