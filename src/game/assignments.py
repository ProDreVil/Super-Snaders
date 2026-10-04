import random

from utils.file import read_txt

MAX_PLAYERS = 4

def input_players():
    while True:
        try:
            player_count = int(input("Enter the amount of players (1~4): "))
            if 1 <= player_count <= MAX_PLAYERS:
                break
            else:
                print("Hey that's not in the range :p")
        except ValueError:
            print("Invalid input dummy >:(")
    return player_count

def assign_turn_order(player_count):
    player_list = [f"Player {i}" for i in range(1, player_count + 1)]
    random.shuffle(player_list)
    turn_order = {}
    for turn, name in enumerate(player_list, start=1):
        turn_order[name] = turn
    print(turn_order)
    return turn_order

def assign_name():
    names = read_txt("./data/names.txt")

def define_stats():
    pass