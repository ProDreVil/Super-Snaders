import random
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))

def create_classic_dice_state():
    return {
        "top_face": None,
        "faces": list(range(1, 7)),
        "weights": {face: 1 for face in range(1, 7)}
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

if __name__ == "__main__":
    dice = create_classic_dice_state()
    print("Before shaking:")
    print("Weights:", dice["weights"])
    print("Roll:", classic_dice_roll(dice))
    top_face = classic_dice_shake(dice)
    print("\nAfter shaking:")
    print("Top face:", top_face)
    print("Weights:", dice["weights"])
    results = [classic_dice_roll(dice) for _ in range(10000)]
    print("Top face occurrences:", results.count(top_face), "/ 10000")