class Item:
    """An object the player can interact with in the game

    Args:
        name: String -- the name of the item
        description: String -- The description of the item
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}\n{self.description}"
