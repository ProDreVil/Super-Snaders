from game.board import create_board
from game.assignments import input_players, assign_turn_order

def prepare_game():
    player_count = input_players()
    create_board(player_count)
    assign_turn_order(player_count)

def player_turn(turn_order):
    pass

def bots_turn(turn_order):
    pass

def turn_loop(turn_order):
    pass

def selection_flow():
    pass