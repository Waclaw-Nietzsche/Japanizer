import pygame as pg
import settings as st

from player import Player

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

        pg.draw.circle(screen, st.GREEN, player.position, 12)

        pg.display.flip()
        clock.tick(st.FPS)

