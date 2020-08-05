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
        self.textures = \
            {
            '1': pg.image.load('textures/wood.png').convert(),
            '2': pg.image.load('textures/floor.png').convert(),
            'S': pg.image.load('textures/sky.png').convert()
            }

    def background(self, angle):
        # Отрисовка "Неба и Земли"
        #pg.draw.rect(self.screen, st.SKYBLUE, (0, 0, st.WINDOW_WIDTH, st.HALF_WINDOW_HEIGHT))
        sky_offset = -5 * math.degrees(angle) % st.WINDOW_WIDTH
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - st.WINDOW_WIDTH, 0))
        self.screen.blit(self.textures['S'], (sky_offset + st.WINDOW_WIDTH, 0))
        pg.draw.rect(self.screen, st.DARKGRAY, (0, st.HALF_WINDOW_HEIGHT, st.WINDOW_WIDTH, st.HALF_WINDOW_HEIGHT))

    def world(self, player_position, player_angle):
        ray_casting(self.screen, player_position, player_angle, self.textures)

    def framerate(self, clock):
        fps = str(int(clock.get_fps()))
        render = self.font.render(fps,0,st.RED)
        self.screen.blit(render, st.FPS_COORDINATES)

    def minimap(self, player):
        self.minimap_screen.fill(st.BLACK)
        map_x, map_y = player.x // st.MINIMAP_SCALE, player.y // st.MINIMAP_SCALE

        # Отрисовка лучей взгляда
        pg.draw.line(self.minimap_screen, st.RED, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                                      map_y + 12 * math.sin(player.angle)), 2)
        # Отрисовка персонажа
        pg.draw.circle(self.minimap_screen, st.YELLOW, (int(map_x), int(map_y)), 5)
        # Отрисовка стен
        for x, y, in mini_game_map:
            pg.draw.rect(self.minimap_screen, st.GREEN, (x, y, st.MINIMAP_TILE, st.MINIMAP_TILE))

        # Размещаем в левом нижнем углу
        self.screen.blit(self.minimap_screen, st.MINIMAP_COORDINATES)
