from mechanics.dice.common_dice import *

def dice_roll(dice_state):
    return classic_dice_roll(dice_state)

def dice_states():
    pass

def use_dice(action, dice_state):
    actions = {"roll": classic_dice_roll, "shake": classic_dice_shake}
    if action not in actions:
        raise ValueError(f"Unknown dice action: {action}")
    return actions[action](dice_state)

def dice_slots():
    pass

def dice_odds(dice_state):
    weights = dice_state["weights"]
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("Total dice weight must be greater than zero.")
    return {face: weight / total_weight * 100 for face, weight in weights.items()}

if __name__ == "__main__":
    dice = create_classic_dice_state()
    print("Initial odds:")
    for face, odds in dice_odds(dice).items():
        print(f"Face {face}: {odds:.2f}%")
    top_face = use_dice("shake", dice)
    print(f"\nTop face after shaking: {top_face}")
    print("Updated odds:")
    for face, odds in dice_odds(dice).items():
        print(f"Face {face}: {odds:.2f}%")
    print("\nRoll result:", use_dice("roll", dice))