from room import Room
from player import Player

room = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons", []
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

# Activate the game globally
# TODO: come up with a non-global way of doing this
game_active = True


def bad_move():
    print("You can not go that way")


def analize_input(player, user_input):
    global game_active
    command = list(user_input.strip().replace(" ", ""))

    if command[0][0] == "q":
        print("\nAre you sure you wish to quit the game? [Y/N]\n")
        quit_game = input(">")
        if quit_game.lower() == "y":
            game_active = False

    elif command[0][0] == "m":
        if len(command) < 2:
            print("You must include a direction [N/S/E/W] when trying to move")
            return

        elif command[1][0] == "n":
            attempt_move(player, "n")

        elif command[1][0] == "e":
            attempt_move(player, "e")

        elif command[1][0] == "s":
            attempt_move(player, "s")

        elif command[1][0] == "w":
            attempt_move(player, "w")

        else:
            print("You must include a direction [N/S/E/W] when trying to move")
            return

    elif command[0][0] == "l":
        list_controls()


def attempt_move(player, direction):
    print("\nAttempted to move... \n")
    attribute = direction + "_to"

    if hasattr(player.location, attribute):
        next_room = getattr(player.location, attribute)
        player.location = next_room
        return

    else:
        bad_move()


def list_controls():
    print("GAME CONTROLS")
    print("[M]ove: [N]orth, [S]outh, [E]ast, [W]est")
    print("[Q]uit\n")


def main():
    current_room = room["outside"]

    # Prompt the player for a character name
    char_name = input("Please name your hero to begin your quest:\n>")
    player1 = Player(char_name, current_room, [])
    print(f"\nWelcome {player1.name}!\n")

    # List the controls for new players
    list_controls()

    # Run the game "event loop"
    while game_active:

        # Print the current room name
        print(
            f"""
        LOCATION: {player1.location.name}
        -{player1.location.description}-
        """
        )

        # Waits for user decision
        print("What next?")
        print("Type [L]ist to view commands")
        user_input = input("\n>").lower()

        analize_input(player1, user_input)


if __name__ == "__main__":
    main()
