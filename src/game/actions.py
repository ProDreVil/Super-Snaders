from game.log import *
from mechanics.dice.dice import use_dice
from utils.config import MAX_PLAYERS, ROLL_STAMINA_COST, SHAKE_STAMINA_COST

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

def turn_action(current_player, game_state):
    turn_details()
    player = game_state["players"][current_player]
    dice = player["dice"]
    stats = player["stats"]
    mana = stats["Mana"]["value"]["current"]
    stamina = dice["stamina"]["current"]
    can_roll = mana >= dice["roll_cost"] and stamina >= ROLL_STAMINA_COST
    can_shake = mana >= dice["shake_cost"] + dice["roll_cost"] and stamina >= SHAKE_STAMINA_COST + ROLL_STAMINA_COST
    display_action_menu(can_roll, can_shake)
    valid_choices = ["3", "4"]
    if can_roll:
        valid_choices.append("1")
    if can_shake:
        valid_choices.append("2")
    while True:
        choice = input("Choose an action: ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Try again.")

def has_valid_actions(current_player, game_state):
    player = game_state["players"][current_player]
    dice = player["dice"]
    stats = player["stats"]
    mana = stats["Mana"]["value"]["current"]
    stamina = dice["stamina"]["current"]
    can_roll = mana >= dice["roll_cost"] and stamina >= ROLL_STAMINA_COST
    can_shake = mana >= dice["shake_cost"] + dice["roll_cost"] and stamina >= SHAKE_STAMINA_COST + ROLL_STAMINA_COST
    return can_roll or can_shake

def execute_action(current_player, action, game_state):
    if action == "1":
        system_message(f"{current_player} selected Roll Dice.", "ACTION")
        dice_state = game_state["players"][current_player]["dice"]
        result = roll_dice(dice_state, current_player, game_state)
        if isinstance(result, int) and not isinstance(result, bool):
            return {"type": "move", "distance": result}
        if result is None:
            return {"type": "end_turn"}
        return {"type": "continue"}
    elif action == "2":
        system_message(f"{current_player} selected Shake Dice.", "ACTION")
        dice_state = game_state["players"][current_player]["dice"]
        result = shake_dice(dice_state, current_player, game_state)
        if result is None:
            return {"type": "end_turn"}
        return {"type": "continue"}
    elif action == "3":
        system_message(f"{current_player} selected Use a Card.", "ACTION")
        return {"type": "continue"}
    elif action == "4":
        system_message(f"{current_player} skipped their turn.", "ACTION")
        return {"type": "end_turn"}
    return {"type": "continue"}

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
        system_message(
            f"{current_player}'s Shake Dice action failed. "
            f"Mana: {game_state['players'][current_player]['stats']['Mana']['value']['current']}; "
            f"Stamina: {dice_state['stamina']['current']}.", "DEBUG"
        )
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
