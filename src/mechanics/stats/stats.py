from game.log import system_message

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

def replenish_mana(game_state, current_player):
    stats = players_stats(game_state, current_player)
    mana = stats["Mana"]["value"]
    replenishment = stats["Replenishment"]["value"]
    total_mana = mana["current"] + replenishment
    overflow = max(0, total_mana - mana["maximum"])
    mana["current"] = min(total_mana, mana["maximum"])
    if overflow > 0:
        mana_pv = float(stats["Mana"]["point_value"])
        cash_pv = float(stats["Cash"]["point_value"])
        cash_gain = overflow * mana_pv / cash_pv
        stats["Cash"]["value"] += int(cash_gain)
        system_message(f"{current_player} converted {overflow} excess Mana into {int(cash_gain)} Cash.", "REPLENISHMENT")
    system_message(f"{current_player} replenished Mana: {mana['current']}/{mana['maximum']} MP.", "REPLENISHMENT")

def spend_mana(game_state, current_player, amount, reserve=0):
    stats = players_stats(game_state, current_player)
    mana = stats["Mana"]["value"]
    if mana["current"] - amount < reserve:
        return False
    mana["current"] -= amount
    return True

def recover_stamina(dice_state):
    stamina = dice_state["stamina"]
    stamina["current"] = min(stamina["current"] + dice_state["recovery"], stamina["maximum"])
    return stamina["current"]