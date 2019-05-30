from room import Room
from player import Player
from item import Item
from helpers import (
    clear_screen,
    get_character_name,
    info_screen,
    list_controls,
    print_banner,
    process_user_command,
)

room = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons", ["crowbar"]
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south.
        Dusty passages run north and east.""",
        [],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness.
        Ahead to the north, a light flickers in the distance,
        but there is no way across the chasm.""",
        [],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north.
        The smell of gold permeates the air.""",
        [],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber!
        Sadly, it has already been completely emptied by earlier adventurers.
        The only exit is to the south.""",
        [],
    ),
}

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

item = {"crowbar": Item("crowbar", "Useful for breaking boxes open")}


def main():
    current_room = room["outside"]

    # Prompt the player for a character name
    char_name = get_character_name()
    player1 = Player(char_name, current_room)

    # List the controls for new players
    list_controls()

    # Indicate that the user is playing the game now
    playing = True

    # Run the game "event loop"
    while playing:

        # Print the current room name
        info_screen(player1)

        # Waits for user decision
        print("What next?")
        print("Type [L]ist to view commands")
        user_input = input("\n> ").lower()

        playing = process_user_command(player1, user_input, playing)


if __name__ == "__main__":
    main()
