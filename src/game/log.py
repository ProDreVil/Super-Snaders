from datetime import datetime
import os

LOG_ENTRIES = []

def start_log():
    LOG_ENTRIES.clear()
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    log_path = os.path.join(project_root, "data", "system", "log.txt")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "w", encoding="utf-8") as file:
        pass

def save_log():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    log_path = os.path.join(project_root, "data", "system", "log.txt")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as file:
        for entry in LOG_ENTRIES:
            file.write(entry + "\n")
    LOG_ENTRIES.clear()

def system_message(message, message_type="SYSTEM"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"({timestamp}) [{message_type}] {message}"
    LOG_ENTRIES.append(entry)
    print(f"[{message_type}] {message}")
    save_log()

def display_action_menu():
    print("1. Roll Dice")
    print("2. Shake Dice")
    print("3. Use a Card")
    print("4. Skip Turn")

def turn_details():
    pass

def round_details():
    pass

def player_details():
    pass

def print_stats():
    pass

def print_dice_odds(dice_state, player, label="Current odds"):
    weights = dice_state["weights"]
    total_weight = sum(weights.values())
    if total_weight <= 0:
        system_message(f"{player} dice odds cannot be calculated: invalid total weight.", "ERROR")
        return
    odds = ", ".join(
        f"{face}={weight / total_weight * 100:.2f}%"
        for face, weight in sorted(weights.items())
    )
    system_message(f"{player} {label}: {odds}", "DICE")