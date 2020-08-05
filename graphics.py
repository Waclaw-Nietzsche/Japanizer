import math
import pygame as pg
import settings as st

from raycasting import ray_casting
from gamemap import game_world_map, mini_game_map

class Draw:
    def __init__(self, screen, minimap_screen):
        self.screen = screen
        self.minimap_screen = minimap_screen
        self.font = pg.font.SysFont('dejavusans',36,bold=True)
        self.texture = pg.image.load('textures/wood.png').convert()
    def background(self):
        # Отрисовка "Неба и Земли"
        pg.draw.rect(self.screen, st.SKYBLUE, (0, 0, st.WINDOW_WIDTH, st.HALF_WINDOW_HEIGHT))
        pg.draw.rect(self.screen, st.DARKGRAY, (0, st.HALF_WINDOW_HEIGHT, st.WINDOW_WIDTH, st.HALF_WINDOW_HEIGHT))

    def world(self, player_position, player_angle):
        ray_casting(self.screen, player_position, player_angle, self.texture)

    def framerate(self, clock):
        fps = str(int(clock.get_fps()))
        render = self.font.render(fps,0,st.RED)
        self.screen.blit(render, st.FPS_COORDINATES)

    def minimap(self, player):
        self.minimap_screen.fill(st.BLACK)
        map_x, map_y = player.x // st.MINIMAP_SCALE, player.y // st.MINIMAP_SCALE
        # Отрисовка персонажа
        pg.draw.circle(self.minimap_screen, st.GREEN, (int(map_x), int(map_y)), 5)
        # Отрисовка лучей взгляда
        pg.draw.line(self.minimap_screen, st.YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                               map_y + 12 * math.sin(player.angle)), 2)
        # Отрисовка стен
        for x, y, in mini_game_map:
            pg.draw.rect(self.minimap_screen, st.GREEN, (x, y, st.MINIMAP_TILE, st.MINIMAP_TILE))

        # Размещаем в левом нижнем углу
        self.screen.blit(self.minimap_screen, st.MINIMAP_COORDINATES)
