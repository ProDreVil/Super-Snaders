from game.log import turn_details
from utils.config import MAX_PLAYERS

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

def turn_action():
    turn_details()
    print("Your Turn")

def roll_dice():
    pass

def shake_dice():
    pass

def skip_turn():
    pass

def selection_action():
    pass

def open_shop():
    pass
