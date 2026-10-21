from game.actions import execute_action, has_valid_actions, turn_action
from game.board import move_player
from game.log import system_message
from mechanics.stats.stats import recover_stamina

def winner():
    pass

def death():
    pass

def process_turn(current_player, game_state, action_selector, is_bot=False):
    player_state = game_state["players"][current_player]
    board_size = game_state["board_size"]
    turn_type = " (Bot)" if is_bot else ""
    print(f"--- {current_player}'s Turn{turn_type} ---")
    system_message(f"{current_player} is at tile {player_state['position']}/{board_size}.", "POSITION")
    for player_name, state in game_state["players"].items():
        stamina = recover_stamina(state["dice"])
        system_message(f"{player_name} recovered Stamina: {stamina}/{state['dice']['stamina']['maximum']}.", "STAMINA")
    while True:
        if not has_valid_actions(current_player, game_state):
            system_message(f"{current_player} has no valid actions left. Turn skipped.", "ACTION")
            break
        choice = turn_action(current_player, game_state) if action_selector == turn_action else action_selector()
        result = execute_action(current_player, choice, game_state)
        if result["type"] == "move":
            move_player(current_player, result["distance"], game_state)
            break
        if result["type"] == "end_turn":
            return
        print(f"Position: {player_state['position']}/{board_size}")

def player_turn(current_player, game_state):
    process_turn(current_player, game_state, turn_action)

def fall_snake():
    pass

def climb_ladder():
    pass

def fight_players():
    pass