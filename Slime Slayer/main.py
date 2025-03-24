import pygame as pg
import sys
import os
from scripts.entities import physisc_entity
# goes to the utilities folder and imports the utilities file
from utilities.utilities import load_image
class game:
    def  __init__(self):
        # init pygame and create a window
        pg.init()
        # set the window title
        pg.display.set_caption("slime hunter")
        # set the window size
        self.window = pg.display.set_mode((640,480))
        self.clock = pg.time.Clock()
        self.player = physisc_entity(self,'player', (50,50), (8,15))
        self.movement = [False, False]
        # create a empty image
        self.display = pg.Surface((320,240))
        self.assets = {
            'player': load_image('charater model top.png'),
            'cloud' : load_image('blue cloud.png')
        }

        


    def run(self):
        while True:
            # fill the window with a color
            self.window.fill((14,219,248))
            # update the player position and render it
            self.player.update((self.movement[1]- self.movement[0],0))
            self.player.render(self.window)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    #quit pygame
                    pg.quit()
                    #sys exit, exit applicatoin
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False
                    
            pg.display.update()
            # set the frame rate to 60 fps
            self.clock.tick(60)






game().run()
