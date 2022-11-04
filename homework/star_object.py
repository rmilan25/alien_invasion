import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #Load star
        self.image = pygame.image.load('../images/star.png')
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.y += 1 # drop a bit
