import settings as st

game_text_map = \
    [
        'BBBBBBBB',
        'B..B...B',
        'B......B',
        'B....B.B',
        'B......B',
        'BBBBBBBB',
    ]

game_world_map = set()
for j, row in enumerate(game_text_map):
    for i, char in enumerate(row):
        if char == 'B':
            game_world_map.add((i * st.TILE_SIZE, j * st.TILE_SIZE))