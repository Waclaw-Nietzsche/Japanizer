import math
import pygame as pg
import settings as st
from gamemap import game_world_map

# Проецирование лучей в лоб, попиксельно (неоптимально)
def ray_casting_old(screen, player_position, player_angle):
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
                c = 255 / (1 + depth * depth * 0.00002)
                color = (c,c,c)
                pg.draw.rect(screen, color, (ray * st.SCALE_OF_VIEW,
                                                st.HALF_WINDOW_HEIGHT - projection_height // 2,
                                                st.SCALE_OF_VIEW,
                                                projection_height))
                break
        current_angle += st.DELTA_OF_ANGLE

def corner(a,b):
    return (a // st.TILE_SIZE) * st.TILE_SIZE, (b // st.TILE_SIZE) * st.TILE_SIZE

# Алгоритм Брезенхэма
def ray_casting(screen, player_position, player_angle):
    x0, y0 = player_position
    # Левый верхний угол текущего квадрата
    xm, ym = corner(x0,y0)
    current_angle = player_angle - st.HALF_FOV
    for ray in range(st.RAY_AMOUNT):
        sin_angle = math.sin(current_angle)
        cos_angle = math.cos(current_angle)

        # Пересечения с вериткалями
        if cos_angle >= 0:
            # Текущая вертикаль
            x = xm + st.TILE_SIZE
            dx = 1
        else:
            x = xm
            dx = -1

        # Пройдемся по ширине экрана с интервалами в сторону квадрата карты
        for i in range(0, st.WINDOW_WIDTH, st.TILE_SIZE):
            depth_vertical = (x - x0) / cos_angle
            y = y0 + depth_vertical * sin_angle
            if corner(x + dx, y) in game_world_map:
                break
            x += dx * st.TILE_SIZE


        # Пересечения с горизонталями
        if sin_angle >= 0:
            # Текущая горизонталь
            y = ym + st.TILE_SIZE
            dy = 1
        else:
            y = ym
            dy = -1

        # Пройдемся по ширине экрана с интервалами в сторону квадрата карты
        for i in range(0, st.WINDOW_HEIGHT, st.TILE_SIZE):
            depth_horizontal = (y - y0) / sin_angle
            x = x0 + depth_horizontal * cos_angle
            if corner(x, y + dy) in game_world_map:
                break
            y += dy * st.TILE_SIZE

        # Проекция
        depth = depth_vertical if depth_vertical < depth_horizontal else depth_horizontal
        # Убираем эффект рыбьего глаза (выпуклых стен)
        depth *= math.cos(player_angle - current_angle)
        projection_height = st.PROJECTION_COEFFICIENT / depth
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c, c)
        pg.draw.rect(screen, color, (ray * st.SCALE_OF_VIEW,
                                     st.HALF_WINDOW_HEIGHT - projection_height // 2,
                                     st.SCALE_OF_VIEW,
                                     projection_height))

        current_angle += st.DELTA_OF_ANGLE