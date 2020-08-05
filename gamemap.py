import settings as st

game_text_map = \
    [
        '111111111111',
        '1.1.....1..1',
        '1....2.2...1',
        '1.1........1',
        '1....2.1...1',
        '111111111111',
    ]

game_world_map = {}
mini_game_map = set()
for j, row in enumerate(game_text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_game_map.add((i * st.MINIMAP_TILE, j * st.MINIMAP_TILE))
            if char == '1':
                game_world_map[(i * st.TILE_SIZE, j * st.TILE_SIZE)] = '1'
            elif char == '2':
                game_world_map[(i * st.TILE_SIZE, j * st.TILE_SIZE)] = '2'