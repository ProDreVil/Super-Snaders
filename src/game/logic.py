from game.actions import execute_action, turn_action, skip_turn

def winner():
    pass

def death():
    pass

def player_turn(current_player, game_state):
    player_state = game_state["players"][current_player]
    board_size = game_state["board_size"]
    print(f"\n--- {current_player}'s Turn ---")
    while True:
        choice = turn_action()
        turn_ended = execute_action(current_player, choice, game_state)
        if turn_ended:
            break
        if choice == "1":
            break
        elif choice == "2":
            print(f"Position: {player_state['position']}/{board_size}")

def detect_position(position, movement, board_size):
    new_position = position + movement
    return min(new_position, board_size)

def fall_snake():
    pass

def climb_ladder():
    pass

def fight_players():
    pass