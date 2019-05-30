import os
from time import sleep


def get_character_name():
    clear_screen()
    char_name = input("Please name your hero to begin your quest:\n> ")
    clear_screen()
    print_banner(f"\nWelcome {char_name}!\n")
    return char_name


def clear_screen():
    """Clear the terminal to clean up display"""
    os.system("cls" if os.name == "nt" else "clear")


def print_banner(message: str, border: str = "-"):
    """ Print an important message with a border

    Args:
        message: String -- The message you'd like printed
        [border]: String -- A single character you want to border the message
    """
    decorator = border * 80
    print(decorator)
    print(message)
    print(decorator)


def list_controls():
    clear_screen()
    print("-" * 80)
    print("GAME CONTROLS")
    print("[M]ove your character: [N]orth, [S]outh, [E]ast, or [W]est")
    print("[I]tem: [G]rab, [D]rop, [L]ist inventory")
    print("[Q]uit the game\n")


def info_screen(player: dict):
    print_banner(f"LOCATION: {player.current_room}")
    print("- Items in reach: ", player.current_room.inventory, "-\n")


def attempt_move(player, direction):
    clear_screen()
    print_banner("\nAttempting to move... \n")
    sleep(0.5)
    clear_screen()
    attribute = direction + "_to"

    if hasattr(player.current_room, attribute):
        next_room = getattr(player.current_room, attribute)
        player.current_room = next_room
        return

    else:
        clear_screen()
        print_banner("You can not go that way")
        sleep(0.5)
        clear_screen()


def process_user_command(player, user_input, active_game):
    command = list(user_input.strip().replace(" ", ""))
    print(command)

    # Handle empty input from user
    if not command:
        clear_screen()
        return True

    # Handle [q]uit command
    if command[0][0] == "q":
        print("\nAre you sure you wish to quit the game? [Y/N]\n")
        quit_game = input("> ")
        if quit_game.lower() == "y":
            return False

    # Handle [M]ovement commands
    elif command[0][0] == "m":
        if len(command) < 2:
            print("You must include a direction [N/S/E/W] when trying to move")

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

    # # Handle [I]nventory commands
    # if command[0][0] == 'i':

    # Handle [L]ist command to view controls
    elif command[0][0] == "l":
        list_controls()

    return True
