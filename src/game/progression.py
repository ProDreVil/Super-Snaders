from game.actions import input_players
from game.assignments import assign_turn_order
from game.board import create_board
from game.logic import player_turn, bot_turn

def start_game():
    current_turn = 0
    player_count = input_players()
    create_board(player_count)
    turn_order, player_list = assign_turn_order(player_count)
    game_loop(player_count, turn_order, player_list, current_turn)

def game_loop(player_count, turn_order, player_list, current_turn):
    turn_loop(turn_order, player_count, current_turn)

def turn_loop(turn_order, player_count, current_turn):
    current_turn += 1
    for i in range(1, player_count + 1):
        current_player = turn_order[i]
        player_turn(current_player) if current_player == "Player 1" else bot_turn(current_player)

def end_game():
    print("\nTHIS IS THE END")
    pass