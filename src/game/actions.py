from game.log import display_action_menu, system_message, turn_details
from mechanics.dice.dice import dice_roll
from utils.config import MAX_PLAYERS

def input_players():
    while True:
        try:
            player_count = int(input("Enter the amount of players (1~4): "))
            if 1 <= player_count <= MAX_PLAYERS:
                break
            else:
                print("Hey that's not in the range :p")
        except ValueError:
            print("Invalid input dummy >:(")
    return player_count

def turn_action():
    turn_details()
    display_action_menu()
    while True:
        choice = input("Choose an action: ").strip()
        if choice in ("1", "2", "3", "4"):
            return choice
        print("Invalid choice. Try again.")

def execute_action(current_player, action, game_state):
    if action == "1":
        system_message(f"{current_player} selected Roll Dice.", "ACTION")
        roll_dice()
    elif action == "2":
        system_message(f"{current_player} selected Shake Dice.", "ACTION")
    elif action == "3":
        system_message(f"{current_player} selected Use a Card.", "ACTION")
    elif action == "4":
        system_message(f"{current_player} skipped their turn.", "ACTION")
        return True
    return False

def roll_dice():
    result = dice_roll()
    print(f"You rolled a {result}!")
    return result

def shake_dice():
    pass

def skip_turn():
    print("You skipped your turn.")

def selection_action():
    pass

def reroll_selection():
    pass

def select_boost():
    pass

def roll_boost():
    pass

def select_quirk():
    pass

def select_card():
    pass

def select_rule():
    pass

def open_shop():
    pass
