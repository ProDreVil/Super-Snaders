from game.log import system_message
from mechanics.dice.common_dice import *
from mechanics.stats.stats import spend_mana

def dice_roll(dice_state):
    return classic_dice_roll(dice_state)

def dice_states():
    pass

def use_dice(action, dice_state, game_state, current_player):
    actions = {"roll": classic_dice_roll, "shake": classic_dice_shake}
    if action not in actions:
        raise ValueError(f"Unknown dice action: {action}")
    cost = dice_state[f"{action}_cost"]
    reserve = dice_state["roll_cost"] if action == "shake" else 0
    if not spend_mana(game_state, current_player, cost, reserve):
        if action == "shake":
            print(f"Not enough Mana to shake! You must retain {dice_state['roll_cost']} MP to roll afterward.")
        else:
            print(f"Not enough Mana! This action requires {cost} MP.")
        return None
    system_message(
    f"{current_player} spent {cost} MP to {action} the {dice_state['name']}.", "MANA")
    result = actions[action](dice_state)
    mana = game_state["players"][current_player]["stats"]["Mana"]["value"]
    system_message(f"{current_player}'s remaining Mana: {mana['current']}/{mana['maximum']} MP.", "MANA")
    return result

def dice_slots():
    pass

def dice_odds(dice_state):
    weights = dice_state["weights"]
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("Total dice weight must be greater than zero.")
    return {face: weight / total_weight * 100 for face, weight in weights.items()}