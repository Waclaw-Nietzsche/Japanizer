import pygame as pg
import settings as st

class Player:
    def __init__(self):
        self.x, self.y = st.PLAYER_POS
        self.angle = st.PLAYER_ANGLE

    @property
    def position(self):
        return (self.x, self.y)

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= st.PLAYER_SPEED
        if keys[pg.K_s]:
            self.y += st.PLAYER_SPEED
        if keys[pg.K_a]:
            self.x -= st.PLAYER_SPEED
        if keys[pg.K_d]:
            self.x += st.PLAYER_SPEED
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
        if keys[pg.K_RIGHT]:
            self.angle += 0.02