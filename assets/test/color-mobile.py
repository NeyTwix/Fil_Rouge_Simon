# pygame setup
import pygame as pg
from random import randint

pg.init()
screen = pg.display.set_mode()
pg.display.set_caption("Test code pour curseur tactile")
pg.display.toggle_fullscreen()

pg.mouse.set_cursor()

Blanc = (255, 255, 255)
noir = (0, 0, 0)

display_surface = pg.display.get_surface()
x,y=pg.display.get_window_size()

score=0
font = pg.font.Font('freesansbold.ttf', x//5)
text = font.render(f' {score} ', True, Blanc, noir)
textRect = text.get_rect()
textRect.center = (x // 2, y // 2)

clock = pg.time.Clock()
going = True
while going:
    clock.tick(60)
    #pg.display.flip()
    display_surface.blit(text, textRect)
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            going = False

        if event.type == pg.MOUSEBUTTONDOWN:
            colors=(randint(0,255), randint(0,255), randint(0,255))
            score+=1
            screen.fill(colors)
            text = font.render(f' {score} ', True, colors, noir)
            textRect = text.get_rect()
            textRect.center = (x // 2, y // 2)
            pg.mouse.set_cursor()
    pg.display.update()

pg.quit()
