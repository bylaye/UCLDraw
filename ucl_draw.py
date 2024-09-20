from random import choice

def structure_draw(pots, home, away):
    draws = {}
    all_pots = list(pots.keys())

    for pot in pots:
        for team in pots[pot]:
            draws[team] = {p:{home:None,away:None} for p in all_pots}
    return draws


