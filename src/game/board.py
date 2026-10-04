def create_board(player_count):
    board_size = player_count * 100
    rows = board_size
    cols = 10
    board = [[i + 1 for i in range(cols)] for _ in range(rows)]
    print("Board Size:", board_size)
    randomize_board(board_size)
    return board_size, board

def display_board(board):
    pass

def randomize_board(board_size):
    pass

def deploy_snakes():
    pass

def deploy_ladders():
    pass

def deploy_tiles():
    pass