from game.log import system_message
from mechanics.dice.common_dice import *
from mechanics.stats.stats import spend_mana
from utils.config import ROLL_STAMINA_COST, SHAKE_STAMINA_COST

def dice_roll(dice_state):
    return classic_dice_roll(dice_state)

def dice_states():
    pass

def use_dice(action, dice_state, game_state, current_player):
    actions = {"roll": classic_dice_roll, "shake": classic_dice_shake}
    if action not in actions:
        raise ValueError(f"Unknown dice action: {action}")
    cost = dice_state[f"{action}_cost"]
    stamina_cost = ROLL_STAMINA_COST if action == "roll" else SHAKE_STAMINA_COST
    reserve_mana = dice_state["roll_cost"] if action == "shake" else 0
    reserve_stamina = ROLL_STAMINA_COST if action == "shake" else 0
    mana = game_state["players"][current_player]["stats"]["Mana"]["value"]
    stamina = dice_state["stamina"]
    if mana["current"] - cost < reserve_mana:
        print(f"Not enough Mana to {action} while retaining enough to roll.")
        return None
    if stamina["current"] - stamina_cost < reserve_stamina:
        print(f"Not enough Stamina to {action} while retaining enough to roll.")
        return None
    if not spend_mana(game_state, current_player, cost, reserve_mana):
        return None
    stamina["current"] -= stamina_cost
    system_message(f"{current_player} spent {cost} MP and {stamina_cost} Stamina to {action} the {dice_state['name']}.", "DICE")
    result = actions[action](dice_state)
    system_message(f"{current_player}'s remaining Mana: {mana['current']}/{mana['maximum']} MP; Stamina: {stamina['current']}/{stamina['maximum']}.", "DICE")
    return result

def dice_slots():
    pass

def dice_odds(dice_state):
    weights = dice_state["weights"]
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("Total dice weight must be greater than zero.")
    return {face: weight / total_weight * 100 for face, weight in weights.items()}