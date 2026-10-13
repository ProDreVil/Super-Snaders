import random

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))

from game.log import system_message
from utils.reader import load_primary_stats, parse_stat_value

def assign_players():
    pass

def assign_name():
    # names = load_txt("./data/names.txt")
    pass

def assign_turn_order(player_count):
    player_list = [f"Player {i}" for i in range(1, player_count + 1)]
    random.shuffle(player_list)
    turn_order = {}
    for turn, name in enumerate(player_list, start=1):
        turn_order[turn] = name
    system_message("Turn order: " + " -> ".join(turn_order.values()), "INFO")
    return turn_order, player_list

def define_stats(player_list):
    primary_stats = load_primary_stats()
    player_stats = {}
    for player in player_list:
        player_stats[player] = {}
        for name, stat in primary_stats.items():
            value = parse_stat_value(stat["value"], {"player_count": len(player_list)})
            player_stats[player][name] = {"value": value, "point_value": stat["point_value"]}
    return player_stats

if __name__ == "__main__":
    test_players = ["Player 1", "Player 2", "Player 3"]
    stats = define_stats(test_players)

    for player, player_stats in stats.items():
        print(f"\n--- {player} ---")

        for name, stat in player_stats.items():
            print(
                f"{name}: {stat['value']} "
                f"(Point Value: {stat['point_value']})"
            )