import math
import pygame as pg
import settings as st

from player import Player
from graphics import Draw
from gamemap import game_world_map
from raycasting import ray_casting

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((st.WINDOW_WIDTH, st.WINDOW_HEIGHT))
    minimap_screen = pg.Surface((st.WINDOW_WIDTH // st.MINIMAP_SCALE, st.WINDOW_HEIGHT // st.MINIMAP_SCALE))
    clock = pg.time.Clock()
    player = Player()
    drawing = Draw(screen, minimap_screen)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        player.movement()
        screen.fill(st.BLACK)

        # Отрисовка "Неба и Земли"
        drawing.background()

        # Имитация отрисовки лучей (псевдо 3Д)
        drawing.world(player.position, player.angle)

        # Счётчик FPS
        drawing.framerate(clock)

        # Отрисовка миникарты
        drawing.minimap(player)

        pg.display.flip()
        clock.tick(st.FPS)

