from game.logic import process_turn

def choose_bot_action():
    print("Bot chooses: Roll Dice")
    return "1"

def bot_turn(current_player, game_state):
    process_turn(current_player, game_state, choose_bot_action, is_bot=True)