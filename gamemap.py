import settings as st

game_text_map = \
    [
        'BBBBBBBBBBBB',
        'B.B.....B..B',
        'B....B.B...B',
        'B.B.....B..B',
        'B....B.B...B',
        'BBBBBBBBBBBB',
    ]

game_world_map = set()
mini_game_map = set()
for j, row in enumerate(game_text_map):
    for i, char in enumerate(row):
        if char == 'B':
            game_world_map.add((i * st.TILE_SIZE, j * st.TILE_SIZE))
            mini_game_map.add((i * st.MINIMAP_TILE, j * st.MINIMAP_TILE))