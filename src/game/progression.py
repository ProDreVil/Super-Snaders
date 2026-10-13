from game.actions import input_players
from game.ai import bot_turn
from game.assignments import assign_turn_order
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
    positions = {player: 1 for player in player_list}
    game_loop(player_count, turn_order, player_list, current_turn, positions, board_size)

def game_loop(player_count, turn_order, player_list, current_turn, positions, board_size):
    turn_loop(turn_order, player_count, current_turn, positions, board_size)

def turn_loop(turn_order, player_count, current_turn, positions, board_size):
    current_turn += 1
    system_message(f"Round {current_turn} started.", "ROUND")
    for i in range(1, player_count + 1):
        current_player = turn_order[i]
        if current_player == "Player 1":
            player_turn(current_player, positions, board_size)
        else:
            bot_turn(current_player, positions, board_size)

def end_game():
    system_message("Game ended.")
    save_log()
    print("\nTHIS IS THE END")