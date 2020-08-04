import math
import pygame as pg
import settings as st
from gamemap import game_world_map

def ray_casting(screen, player_position, player_angle):
    current_angle = player_angle - st.HALF_FOV
    x0, y0 = player_position
    for ray in range(st.RAY_AMOUNT):
        sin_angle = math.sin(current_angle)
        cos_angle = math.cos(current_angle)
        for depth in range(st.MAX_DEPTH_OF_VIEW):
            x = x0 + depth * cos_angle
            y = y0 + depth * sin_angle
            # pg.draw.line(screen, st.DARKGRAY, player_position, (x, y), 2)
            if (x // st.TILE_SIZE * st.TILE_SIZE, y // st.TILE_SIZE * st.TILE_SIZE) in game_world_map:
                # Убираем эффект рыбьего глаза (выпуклых стен)
                depth *= math.cos(player_angle - current_angle)
                projection_height = st.PROJECTION_COEFFICIENT / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c,c,c)
                pg.draw.rect(screen, color, (ray * st.SCALE_OF_VIEW,
                                                st.HALF_WINDOW_HEIGHT - projection_height // 2,
                                                st.SCALE_OF_VIEW,
                                                projection_height))
                break
        current_angle += st.DELTA_OF_ANGLE