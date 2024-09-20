import ucl_draw as ucld
from teams import pots

draws = ucld.structure_draw(pots, 'H', 'A')

for draw_team in draws:
    print(draw_team[0], draws[draw_team])

