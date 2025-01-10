import heroes

damage_aliases = ["dps", "dmg", "damage", "duelist"]
tank_aliases = ["tank", "vanguard"]
support_aliases = ["support", "healer", "heal", "strategist"]

def GetOptions(game, category):
    if game == "overwatch":
        if not category:
            return heroes.overwatch_heroes
        elif category in damage_aliases:
            return heroes.overwatch_dps
        elif category in tank_aliases:
            return heroes.overwatch_tank
        elif category in support_aliases:
            return heroes.overwatch_support
        else:
            return ValueError(f"Invalid category {category} in game {game}")
    elif game == "rivals":
        if not category:
            return heroes.marvel_rivals_heroes
        elif category in damage_aliases:
            return heroes.rivals_duelist
        elif category in tank_aliases:
            return heroes.rivals_strategist
        elif category in support_aliases:
            return heroes.rivals_strategist
        else:
            return ValueError(f"Invalid category {category} in game {game}")
    else:
        return ValueError(f"Invalid game {game}")