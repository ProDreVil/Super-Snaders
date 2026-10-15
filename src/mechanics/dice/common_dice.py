import random

from utils.reader import load_stats, parse_stat_value

def create_dice_state(dice_definition, player_count):
    unlisted_stats = load_stats("UNLISTED")
    variables = {"player_count": player_count}
    stamina_stat = unlisted_stats["Stamina"]
    stamina = parse_stat_value(stamina_stat["value"], variables)
    recovery_stat = unlisted_stats["Recovery"]
    recovery = parse_stat_value(recovery_stat["value"], variables)
    faces = list(range(dice_definition["faces"]["min"], dice_definition["faces"]["max"] + 1))
    return {
        "name": dice_definition["name"],
        "top_face": None,
        "faces": faces,
        "weights": {face: 1 for face in faces},
        "stamina": stamina,
        "recovery": recovery,
        "roll_cost": dice_definition["roll_cost"],
        "shake_cost": dice_definition["shake_cost"],
        "descriptions": dice_definition["descriptions"]
    }

def classic_dice_roll(dice_state):
    weights = dice_state["weights"]
    faces = list(weights.keys())
    probabilities = list(weights.values())
    return random.choices(faces, weights=probabilities, k=1)[0]

def classic_dice_shake(dice_state):
    faces = dice_state["faces"]
    shuffled_faces = random.sample(faces, len(faces))
    dice_state["top_face"] = shuffled_faces[0]
    dice_state["weights"] = {face: len(faces) - index for index, face in enumerate(shuffled_faces)}
    return dice_state["top_face"]