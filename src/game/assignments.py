import random

from utils.reader import load_txt

def assign_players():
    pass

def assign_name():
    names = load_txt("./data/names.txt")

def assign_turn_order(player_count):
    player_list = [f"Player {i}" for i in range(1, player_count + 1)]
    random.shuffle(player_list)
    turn_order = {}
    for turn, name in enumerate(player_list, start=1):
        turn_order[turn] = name
    print(turn_order)
    return turn_order, player_list

def define_stats():
    pass