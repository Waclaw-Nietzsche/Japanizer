import math
import pygame as pg
import settings as st

class Player:
    def __init__(self):
        self.x, self.y = st.PLAYER_POS
        self.angle = st.PLAYER_ANGLE

    @property
    def position(self):
        return (self.x, self.y)

    # Движение персонажа
    def movement(self):
        sin_angle = math.sin(self.angle)
        cos_angle = math.cos(self.angle)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.x += st.PLAYER_SPEED * cos_angle
            self.y += st.PLAYER_SPEED * sin_angle
        if keys[pg.K_s]:
            self.x += -st.PLAYER_SPEED * cos_angle
            self.y += -st.PLAYER_SPEED * sin_angle
        if keys[pg.K_a]:
            self.x += st.PLAYER_SPEED * sin_angle
            self.y += -st.PLAYER_SPEED * cos_angle
        if keys[pg.K_d]:
            self.x += -st.PLAYER_SPEED * sin_angle
            self.y += st.PLAYER_SPEED * cos_angle
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
        if keys[pg.K_RIGHT]:
            self.angle += 0.02