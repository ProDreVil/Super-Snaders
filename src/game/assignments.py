import random

from game.log import system_message
from mechanics.dice.common_dice import create_dice_state
from utils.reader import load_dice_definitions, load_stats, parse_stat_value

def assign_players(player_list, player_stats):
    dice_definitions = load_dice_definitions()
    dice_definition = dice_definitions["Classic Dice"]
    players = {}
    for player in player_list:
        players[player] = {
            "stats": player_stats[player],
            "dice": create_dice_state(dice_definition, len(player_list)),
            "position": 1
        }
    return players

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
    primary_stats = load_stats("PRIMARY")
    player_stats = {}
    for player in player_list:
        player_stats[player] = {}
        for name, stat in primary_stats.items():
            value = parse_stat_value(stat["value"], {"player_count": len(player_list)})
            player_stats[player][name] = {"value": value, "point_value": stat["point_value"]}
    return player_stats

def create_game_state(player_count):
    turn_order, player_list = assign_turn_order(player_count)
    player_stats = define_stats(player_list)
    players = assign_players(player_list, player_stats)
    return {
        "player_count": player_count,
        "turn_order": turn_order,
        "player_list": player_list,
        "players": players,
        "current_turn": 0
    }