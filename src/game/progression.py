from game.actions import input_players
from game.ai import bot_turn
from game.assignments import assign_turn_order, define_stats
from game.board import create_board, display_board
from game.log import save_log, start_log, system_message
from game.logic import player_turn

def start_game():
    start_log()
    system_message("New game started.")
    current_turn = 0
    player_count = input_players()
    board_size, board = create_board(player_count)
    display_board(board)
    turn_order, player_list = assign_turn_order(player_count)
    player_stats = define_stats(player_list)
    game_state = {
        "player_count": player_count,
        "board_size": board_size,
        "turn_order": turn_order,
        "player_list": player_list,
        "player_stats": player_stats,
        "positions": {player: 1 for player in player_list},
        "current_turn": 0
    }
    game_loop(game_state)

def game_loop(game_state):
    turn_loop(game_state)

def turn_loop(game_state):
    game_state["current_turn"] += 1
    current_turn = game_state["current_turn"]
    system_message(f"Round {current_turn} started.", "ROUND")
    for i in range(1, game_state["player_count"] + 1):
        current_player = game_state["turn_order"][i]
        if current_player == "Player 1":
            player_turn(current_player, game_state)
        else:
            bot_turn(current_player, game_state)

def end_game():
    system_message("Game ended.")
    save_log()
    print("\nTHIS IS THE END")