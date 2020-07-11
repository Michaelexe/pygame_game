import pygame as pg

#our player's class
class player():
    def __init__(self, velocity, position_x, position_y):
        self.velocity = velocity 
        self.x = position_x
        self.y = position_y
        self.walkcount = 0
        self.left = False
        self.right = False
        self.walkright = [pg.image.load('game/R1.png'), pg.image.load('game/R2.png'), pg.image.load('game/R3.png'), pg.image.load('game/R4.png'), pg.image.load('game/R5.png'), pg.image.load('game/R6.png'), pg.image.load('game/R7.png'), pg.image.load('game/R8.png'), pg.image.load('game/R9.png')]
        self.walkleft = [pg.image.load('game/L1.png'), pg.image.load('game/L2.png'), pg.image.load('game/L3.png'), pg.image.load('game/L4.png'), pg.image.load('game/L5.png'), pg.image.load('game/L6.png'), pg.image.load('game/L7.png'), pg.image.load('game/L8.png'), pg.image.load('game/L9.png')]
        self.char = pg.image.load('game/standing.png')
        self.bigchar = pg.transform.scale(self.char, (100,100))
        self.direction = 0


    #our players ability to move around the screen
    def movement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and self.x > 30:
            self.x -= self.velocity
            self.walkcount += 1
            self.left = True
            self.right = False

        if keys[pg.K_RIGHT] and self.x < 950:
            self.x += self.velocity
            self.walkcount += 1
            self.right = True
            self.left = False

        if keys[pg.K_UP] and self.y > 190:
            self.y -= self.velocity
            self.left = False
            self.right = False

        if keys[pg.K_DOWN] and self.y < 300:
            self.y += self.velocity
            self.left = False
            self.right = False

        if self.walkcount == 26:
            self.walkcount = 0

    
    #the code to make our player appear on the screen
    def draw(self, window):
        if self.left == True:
            self.newimage = pg.transform.scale(self.walkleft[self.walkcount//3], (100, 100))
            window.blit(self.newimage, (self.x, self.y))

        elif self.right == True:
            self.newimage = pg.transform.scale(self.walkright[self.walkcount//3], (100, 100))
            window.blit(self.newimage, (self.x, self.y))

        else:
            window.blit(self.bigchar, (self.x, self.y))


    #the code to tell which direction is the player pointing towards
    def direction(self):
        if self.left == True:
            self.direction = "left"

        elif self.right == True: 
            self.direction = "right"


#the code for importing most of the images into a class and treating them as an object
class images():
    def __init__(self, imagename, position_x, position_y, size_x, size_y):
        self.image = pg.image.load(imagename)
        self.x = position_x
        self.y = position_y
        self.sx = size_x
        self.sy = size_y


    #to make those images show on the screen
    def draw(self, window):
        if self.sx == 0 and self.sy == 0:
            window.blit(self.image, (self.x, self.y))

        else:
            self.smallimage = pg.transform.scale(self.image, (self.sx, self.sy))
            window.blit(self.smallimage, (self.x, self.y))


