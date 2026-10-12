from game.actions import execute_action

def bot_turn(current_player, positions, board_size):
    print(f"\n--- {current_player}'s Turn (Bot) ---")
    print("Bot chooses: Roll Dice")
    execute_action(current_player, "1", positions, board_size)