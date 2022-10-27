import pygame

class BlueBomber:
    def __init__(self):
        self.screen = pygame.display.set_mode((200, 200))
        self.screen.fill((122, 156, 245))
        self.screen_rect = self.screen.get_rect()
        #Load bomber
        self.image = pygame.image.load('../images/blue_bomber.png')
        self.rect = self.image.get_rect()
        #Start at the center
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
    def update_movement(self):
        if self.moving_right and self.rect.right < 200:
            self.x += .1
        elif self.moving_left and self.rect.left > 0:
            self.x -= .1
        elif self.moving_up and self.rect.top > 0:
            self.y -= .1
        elif self.moving_down and self.rect.bottom < 200:
            self.y += .1
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image,self.rect)



