#importing necessary modules
from classes import*
import pygame as pg
pg.init()

clock = pg.time.Clock()

#creating the window and header
window = pg.display.set_mode((1000,400))
pg.display.set_caption("Level_1")

#making necessary objects such as the player
bg = images("game again/bglv1.jpg", 0, 0, 1000, 400)
our_character = player(5, 100, 300)
char_projectile = projectile(10, "game again/fireball.png", our_character.direction, our_character.x, our_character.y, 60, 60, window)

#game loop
run = True
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    clock.tick(27)

    our_character.movement()
    our_character.check_direction()
    char_projectile.shoot()

    #drawing all the objects onto the window
    bg.draw(window)
    our_character.draw(window)
    pg.display.update()

