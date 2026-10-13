from game.log import system_message
from utils.config import BOARD_TILES_MULTIPLIER

def create_board(player_count):
    board_size = player_count * BOARD_TILES_MULTIPLIER
    cols = 10
    rows = board_size // cols
    board = [
        list(range(row * cols + 1, (row + 1) * cols + 1))
        if row % 2 == 0
        else list(range((row + 1) * cols, row * cols, -1))
        for row in range(rows)
    ]
    system_message(f"Board size: {board_size} tiles.", "INFO")
    randomize_board(board_size)
    return board_size, board

def display_board(board):
    print("=" * 60)
    for row in reversed(board):
        print(" | ".join(f"{tile:3}" for tile in row))
    print("=" * 60)

def randomize_board(board_size):
    pass

def deploy_snakes():
    pass

def deploy_ladders():
    pass

def deploy_tiles():
    pass