from game.actions import execute_action

def bot_turn(current_player, game_state):
    print(f"\n--- {current_player}'s Turn (Bot) ---")
    print("Bot chooses: Roll Dice")
    execute_action(current_player, "1", game_state)