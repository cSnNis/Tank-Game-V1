from settings import *
import pygame as pg
from main import *



#Obstacle class for dead tanks/rubble
class DeadTank(pg.sprite.Sprite):
    def __init__(self, game, spawnPosition):
        super().__init__()
        self.game = game
        self.add(game.obs_group)
        self.spawnPosition = spawnPosition #input the dead NPC/Player's center attribute here
        '''We will most likely need to add a new input for which image path to choose 
        (for when there's different colors), for now GD is the default'''
        self.image = pg.image.load(GD_path).convert_alpha(); self.image = pg.transform.scale(self.image, (self.image.get_width() * RESMULTX * tankSpriteScalingFactor, self.image.get_height() * RESMULTY * tankSpriteScalingFactor))
        self.rect = self.image.get_rect(center = spawnPosition)
        