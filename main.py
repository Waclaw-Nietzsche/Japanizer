import math
import pygame as pg
import settings as st

from player import Player
from gamemap import game_world_map
from raycasting import ray_casting

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((st.WINDOW_WIDTH, st.WINDOW_HEIGHT))
    clock = pg.time.Clock()
    player = Player()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        player.movement()
        screen.fill(st.BLACK)

        # Отрисовка "Неба и Земли"
        pg.draw.rect(screen, st.BLUE, (0,0,st.WINDOW_WIDTH, st.HALF_WINDOW_HEIGHT))
        pg.draw.rect(screen, st.DARKGRAY, (0, st.HALF_WINDOW_HEIGHT, st.WINDOW_WIDTH, st.HALF_WINDOW_HEIGHT))

        # Имитация отрисовки лучей (псевдо 3Д)
        ray_casting(screen, player.position, player.angle)

        # Отрисовка персонажа
        #pg.draw.circle(screen, st.GREEN, (int(player.x), int(player.y)), 12)
        # Отрисовка лучей взгляда
        #pg.draw.line(screen, st.GREEN, player.position,
        #             (player.x + st.WINDOW_WIDTH * math.cos(player.angle),
        #             (player.y + st.WINDOW_WIDTH * math.sin(player.angle))))
        # Отрисовка стен
        #for x, y, in game_world_map:
        #    pg.draw.rect(screen, st.DARKGRAY, (x, y, st.TILE_SIZE, st.TILE_SIZE), 2)
        pg.display.flip()
        clock.tick(st.FPS)

