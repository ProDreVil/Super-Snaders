from game.actions import input_players
from game.ai import bot_turn
from game.assignments import create_game_state
from game.board import create_board, display_board
from game.log import save_log, start_log, system_message
from game.logic import player_turn
from mechanics.stats.stats import replenish_mana
from utils.config import MAX_ROUNDS

def start_game():
    start_log()
    system_message("New game started.")
    current_turn = 0
    player_count = input_players()
    board_size, board = create_board(player_count)
    display_board(board)
    game_state = create_game_state(player_count)
    game_state["board_size"] = board_size
    game_loop(game_state)

def game_loop(game_state):
    while game_state["current_turn"] < MAX_ROUNDS:
        turn_loop(game_state)
    system_message(f"Reached the temporary limit of {MAX_ROUNDS} rounds.", "INFO")

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
    for current_player in game_state["player_list"]:
        replenish_mana(game_state, current_player)

def end_game():
    system_message("Game ended.")
    save_log()
    print("\nTHIS IS THE END")