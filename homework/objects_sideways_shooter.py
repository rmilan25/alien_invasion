import pygame
from pygame.sprite import Sprite

class SideShooter:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill((128, 0, 0))
        self.screen_rect = self.screen.get_rect()
        #Load bomber
        self.image = pygame.image.load('../images/side_shooter.png')
        self.rect = self.image.get_rect()
        #Start at the center
        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
    def update_movement(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= .1
        elif self.moving_down and self.rect.bottom < 400:
            self.y += .1
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image,self.rect)

class Bullet(Sprite):

    def __init__(self,homework_game):
        super().__init__()
        self.screen = pygame.display.set_mode((400, 400))

        self.bullet_speed = .01
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255,255,255)

        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.rect.center = homework_game.side_shooter.rect.center

        self.x = float(self.rect.x)
    def update(self):
        self.x += self.bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)
