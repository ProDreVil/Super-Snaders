from game.log import *
from mechanics.dice.dice import use_dice
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
        dice_state = game_state["players"][current_player]["dice"]
        roll_dice(dice_state, current_player, game_state)
    elif action == "2":
        system_message(f"{current_player} selected Shake Dice.", "ACTION")
        dice_state = game_state["players"][current_player]["dice"]
        shake_dice(dice_state, current_player, game_state)
    elif action == "3":
        system_message(f"{current_player} selected Use a Card.", "ACTION")
    elif action == "4":
        system_message(f"{current_player} skipped their turn.", "ACTION")
        return True
    return False

def roll_dice(dice_state, current_player, game_state):
    print_dice_odds(dice_state, current_player)
    result = use_dice("roll", dice_state, game_state, current_player)
    if result is None:
        return None
    system_message(f"{current_player} rolled {result}.", "DICE")
    return result

def shake_dice(dice_state, current_player, game_state):
    print_dice_odds(dice_state, current_player, "Odds before shake")
    top_face = use_dice("shake", dice_state, game_state, current_player)
    if top_face is None:
        return None
    system_message(
        f"{current_player} shook the dice. Top face: {top_face}; "
        f"weights: {dice_state['weights']}", "DICE")
    print_dice_odds(dice_state, current_player, "Odds after shake")
    return top_face

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
