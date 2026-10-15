def players_stats(game_state, current_player):
    return game_state["players"][current_player]["stats"]

def change_health(game_state, current_player, amount):
    stats = players_stats(game_state, current_player)
    health = stats["Health"]["value"]
    health["current"] += amount
    health["current"] = max(0, min(health["current"], health["maximum"]))
    return health["current"]

def change_mana(game_state, current_player, amount):
    stats = players_stats(game_state, current_player)
    mana = stats["Mana"]["value"]
    if mana["current"] + amount < 0:
        return False
    mana["current"] = min(mana["current"] + amount, mana["maximum"])
    return mana["current"]

def spend_mana(game_state, current_player, amount, reserve=0):
    stats = players_stats(game_state, current_player)
    mana = stats["Mana"]["value"]
    if mana["current"] - amount < reserve:
        return False
    mana["current"] -= amount
    return True